from __future__ import annotations

import logging
import random

from gensec.basic_logging import BasicLogger


class NaiveHeuristics:
    def __init__(self, seed: int = 42, level: int = logging.INFO) -> None:
        self.logger = BasicLogger(name="bl_naive_heuristics", level=level).logger
        self.seed = seed

    def count_punctuation_chars(self, hypothesis: str) -> int:
        return sum(1 for char in hypothesis if char in ["!", "?", ".", ",", ";", ":", "-", "$", "%", "&"])

    def naive_selection(self, all_candidates: list[list[str]], metric_name: str) -> list[str]:
        assert all_candidates, "The input list cannot be empty."
        assert all(all_candidates), "The input list cannot contain empty lists."

        all_candidates = [list(filter(None, hypotheses)) for hypotheses in all_candidates]

        res = []
        for hypotheses in all_candidates:
            if metric_name == "longest":
                # if there are multiple candidates with the same length, the first one is selected
                max_length_hypothesis = max(hypotheses, key=lambda x: len(x.replace(" ", "")))
                res.append(max_length_hypothesis)

            elif metric_name == "shortest":
                # if there are multiple candidates with the same length, the first one is selected
                min_length_hypothesis = min(hypotheses, key=lambda x: len(x.replace(" ", "")))
                res.append(min_length_hypothesis)

            elif metric_name == "most_punctuation":
                # if there are multiple candidates with the same number of punctuation characters, the first one is selected
                most_punctuation_hypothesis = max(hypotheses, key=self.count_punctuation_chars)
                res.append(most_punctuation_hypothesis)

            elif metric_name == "least_punctuation":
                # if there are multiple candidates with the same number of punctuation characters, the first one is selected
                least_punctuation_hypothesis = min(hypotheses, key=self.count_punctuation_chars)
                res.append(least_punctuation_hypothesis)

            elif metric_name == "random":
                random.seed(self.seed)
                random_hypothesis = random.choice(hypotheses)
                res.append(random_hypothesis)

            elif metric_name == "longest_and_most_punctuation":
                max_length_hypothesis = max(hypotheses, key=lambda x: len(x.replace(" ", "")))
                candidates_with_max_length = [
                    h for h in hypotheses if len(h.replace(" ", "")) == len(max_length_hypothesis.replace(" ", ""))
                ]
                most_punctuation_hypothesis = max(candidates_with_max_length, key=self.count_punctuation_chars)
                res.append(most_punctuation_hypothesis)

            elif metric_name == "shortest_and_least_punctuation":
                min_length_hypothesis = min(hypotheses, key=lambda x: len(x.replace(" ", "")))
                candidates_with_min_length = [
                    h for h in hypotheses if len(h.replace(" ", "")) == len(min_length_hypothesis.replace(" ", ""))
                ]
                least_punctuation_hypothesis = min(candidates_with_min_length, key=self.count_punctuation_chars)
                res.append(least_punctuation_hypothesis)

            elif metric_name == "longest_and_least_punctuation":
                max_length_hypothesis = max(hypotheses, key=lambda x: len(x.replace(" ", "")))
                candidates_with_max_length = [
                    h for h in hypotheses if len(h.replace(" ", "")) == len(max_length_hypothesis.replace(" ", ""))
                ]
                least_punctuation_hypothesis = min(candidates_with_max_length, key=self.count_punctuation_chars)
                res.append(least_punctuation_hypothesis)

            elif metric_name == "shortest_and_most_punctuation":
                min_length_hypothesis = min(hypotheses, key=lambda x: len(x.replace(" ", "")))
                candidates_with_min_length = [
                    h for h in hypotheses if len(h.replace(" ", "")) == len(min_length_hypothesis.replace(" ", ""))
                ]
                most_punctuation_hypothesis = max(candidates_with_min_length, key=self.count_punctuation_chars)
                res.append(most_punctuation_hypothesis)

            else:
                msg = f"Metric {metric_name} is not implemented."
                raise NotImplementedError(msg)

        assert res, "The reranked list is empty."
        assert len(res) == len(all_candidates), "The reranked list has a different length from the input list."

        return res
