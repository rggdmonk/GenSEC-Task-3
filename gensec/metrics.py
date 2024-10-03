from __future__ import annotations

import logging

import jiwer
from sacrebleu.metrics import CHRF, TER

from gensec.basic_logging import BasicLogger


class MetricsBase:
    def __init__(self, logger_name: str) -> None:
        self.logger = BasicLogger(name=logger_name, level=logging.DEBUG).logger

    def _calculate_jiwer_metric(
        self, metric_function: callable, hypothesis: str | list[str], reference: str | list[str]
    ) -> float:
        return metric_function(
            reference=reference,
            hypothesis=hypothesis,
            reference_transform=jiwer.wer_default,
            hypothesis_transform=jiwer.wer_default,
        )


class MetricsLowerIsBetter(MetricsBase):
    def __init__(self) -> None:
        super().__init__("bl_metrics_lower")
        self.default_ter = TER(normalized=False, no_punct=False, asian_support=False, case_sensitive=False)

    def get_score_ter(self, hypothesis: str, reference: list[str]) -> float:
        """
        Translation Error Rate (TER) -- Lower is better.
        """
        return self.default_ter.sentence_score(hypothesis, reference).score

    def get_score_wer(self, hypothesis: str | list[str], reference: str | list[str]) -> float:
        """
        word error rate (WER) -- Lower is better.
        This value indicates the percentage of words that were incorrectly predicted.
        """
        return self._calculate_jiwer_metric(jiwer.wer, hypothesis, reference)

    def get_score_mer(self, hypothesis: str | list[str], reference: str | list[str]) -> float:
        """
        match error rate (MER) -- Lower is better.
        This value indicates the percentage of words that were incorrectly predicted and inserted.
        """
        return self._calculate_jiwer_metric(jiwer.mer, hypothesis, reference)

    def get_score_wil(self, hypothesis: str | list[str], reference: str | list[str]) -> float:
        """
        word information loss (WIL) -- Lower is better.
        This value indicates the percentage of words that were incorrectly predicted between a set of ground-truth sentences and a set of hypothesis sentences.
        """
        return self._calculate_jiwer_metric(jiwer.wil, hypothesis, reference)


class MetricsHigherIsBetter(MetricsBase):
    def __init__(self) -> None:
        super().__init__("bl_metrics_higher")
        self.default_chrf = CHRF(
            char_order=6, word_order=0, beta=1, lowercase=False, whitespace=False, eps_smoothing=False
        )
        self.default_chrf_plus_plus = CHRF(
            char_order=6, word_order=2, beta=1, lowercase=False, whitespace=False, eps_smoothing=False
        )

    def get_score_chrf(self, hypothesis: str, reference: list[str]) -> float:
        """
        chrF -- Higher is better.
        """
        return self.default_chrf.sentence_score(hypothesis, reference).score

    def get_score_chrf_plus_plus(self, hypothesis: str, reference: list[str]) -> float:
        """
        chrF++ -- Higher is better.
        """
        return self.default_chrf_plus_plus.sentence_score(hypothesis, reference).score

    def get_score_wip(self, hypothesis: str | list[str], reference: str | list[str]) -> float:
        """
        word information preservation (WIP) -- Higher is better.
        This value indicates the percentage of words that were correctly predicted between a set of ground-truth sentences and a set of hypothesis sentences.
        """
        return self._calculate_jiwer_metric(jiwer.wip, hypothesis, reference)
