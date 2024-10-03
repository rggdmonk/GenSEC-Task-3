from __future__ import annotations

import logging

from gensec.basic_logging import BasicLogger
from gensec.metrics import MetricsHigherIsBetter, MetricsLowerIsBetter


class RerankerBase:
    def __init__(self, logger_name: str, level: int = logging.DEBUG) -> None:
        self.logger = BasicLogger(name=logger_name, level=level).logger
        # Initialize metrics classes here or ensure derived classes do
        self.reranker_metrics_higher_is_better = None
        self.reranker_metrics_lower_is_better = None

    def _standardize_metric_name(self, metric_name: str) -> str:
        """Standardize the metric name to match the method name.
        Example: chrf++ -> get_score_chrf_plus_plus
        Example: chrf -> get_score_chrf
        Example: mer -> get_score_mer
        """
        if metric_name.lower() == "chrf++".lower():
            return "get_score_chrf_plus_plus"

        return f"get_score_{metric_name}"

    def _calculate_accumulated_scores(
        self, hypotheses: list[str], standartized_metric_name: str = "get_score_chrf_plus_plus"
    ) -> list[float]:
        """Calculate the accumulated scores for each hypothesis."""

        # Determine which metrics class to use based on the metric name
        if standartized_metric_name in self._get_metric_methods(metrics_class=self.reranker_metrics_higher_is_better):
            metric_usage = getattr(self.reranker_metrics_higher_is_better, standartized_metric_name)
        elif standartized_metric_name in self._get_metric_methods(metrics_class=self.reranker_metrics_lower_is_better):
            metric_usage = getattr(self.reranker_metrics_lower_is_better, standartized_metric_name)
        else:
            msg = f"Metric {standartized_metric_name} is not implemented."
            raise NotImplementedError(msg)

        accumulated_scores = [0] * len(hypotheses)
        for i in range(len(hypotheses)):
            for j in range(len(hypotheses)):
                if i == j:  # We do not evaluate a hypothesis against itself
                    continue
                score_i_against_j = metric_usage(hypotheses[i], [hypotheses[j]])
                msg_score_i_against_j = f"Score of hypothesis {i} against hypothesis {j}: {score_i_against_j}"
                self.logger.debug(msg_score_i_against_j)
                accumulated_scores[i] += score_i_against_j

        return accumulated_scores

    def _get_metric_methods(self, metrics_class: MetricsHigherIsBetter | MetricsLowerIsBetter) -> list[str]:
        """Retrieve all metric methods from a metrics class."""
        return [
            method
            for method in dir(metrics_class)
            if callable(getattr(metrics_class, method)) and not method.startswith("__")
        ]

    def _select_best_hypothesis_max(self, hypotheses: list[str], accumulated_scores: list[float]) -> str:
        """Select the hypothesis with the highest accumulated score."""
        max_index = accumulated_scores.index(max(accumulated_scores))
        return hypotheses[max_index]

    def _select_best_hypothesis_min(self, hypotheses: list[str], accumulated_scores: list[float]) -> str:
        """Select the hypothesis with the lowest accumulated score."""
        min_index = accumulated_scores.index(min(accumulated_scores))
        return hypotheses[min_index]


class Reranker(RerankerBase):
    def __init__(self, level: int = logging.INFO) -> None:
        super().__init__(logger_name="bs_reranker", level=level)

        self.reranker_metrics_higher_is_better = MetricsHigherIsBetter()
        self.reranker_metrics_lower_is_better = MetricsLowerIsBetter()

    def rerank(self, all_candidates: list[list[str]], metric_name: str = "chrf_plus_plus") -> list[str]:
        """Rerank all the hypotheses inside a beam based on inter-hypothesis similarity."""
        self.logger.debug("Reranking hypotheses.")

        assert all_candidates, "The input list cannot be empty."
        assert all(all_candidates), "The input list cannot contain empty lists."

        msg = f"Using metric: {metric_name}"
        self.logger.debug(msg)

        metric_name = self._standardize_metric_name(metric_name)

        msg = f"Using metric (standardized): {metric_name}"
        self.logger.debug(msg)

        # remove empty strings from lst
        all_candidates = [list(filter(None, hypotheses)) for hypotheses in all_candidates]

        res = []
        for hypotheses in all_candidates:
            accumulated_scores = self._calculate_accumulated_scores(
                hypotheses=hypotheses, standartized_metric_name=metric_name
            )
            msg_accumulated_scores = f"Accumulated scores for all hypotheses: {accumulated_scores}"
            self.logger.debug(msg_accumulated_scores)
            # Find the highest accumulated score
            # If multiple hypotheses have the same accumulated score, tie-breaker is the original position of the hypothesis in the beam
            if metric_name in self._get_metric_methods(metrics_class=self.reranker_metrics_higher_is_better):
                best_hypothesis = self._select_best_hypothesis_max(hypotheses, accumulated_scores)

            elif metric_name in self._get_metric_methods(metrics_class=self.reranker_metrics_lower_is_better):
                best_hypothesis = self._select_best_hypothesis_min(hypotheses, accumulated_scores)
            else:
                msg = f"Metric {metric_name} is not implemented."
                raise NotImplementedError(msg)

            res.append(best_hypothesis)

        assert res, "The reranked list is empty."
        assert len(res) == len(all_candidates), "The reranked list has a different length from the input list."

        return res
