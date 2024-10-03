from __future__ import annotations

from gensec.metrics import MetricsHigherIsBetter, MetricsLowerIsBetter

if __name__ == "__main__":
    awesome_reference = "This is an awesome reference sentence."
    awesome_hypothesis = "This is an awesome hypothesis sentence."

    awesome_ranker_lower = MetricsLowerIsBetter()

    print(f"TER: {awesome_ranker_lower.get_score_ter(awesome_hypothesis, [awesome_reference])}")
    print(f"WER: {awesome_ranker_lower.get_score_wer(awesome_hypothesis, [awesome_reference])}")
    print(f"MER: {awesome_ranker_lower.get_score_mer(awesome_hypothesis, [awesome_reference])}")
    print(f"WIL: {awesome_ranker_lower.get_score_wil(awesome_hypothesis, [awesome_reference])}")

    awesome_ranker_higher = MetricsHigherIsBetter()

    print(f"chrF: {awesome_ranker_higher.get_score_chrf(awesome_hypothesis, [awesome_reference])}")
    print(f"chrF++: {awesome_ranker_higher.get_score_chrf_plus_plus(awesome_hypothesis, [awesome_reference])}")
    print(f"WIP: {awesome_ranker_higher.get_score_wip(awesome_hypothesis, [awesome_reference])}")
