import pytest

from gensec.rerank_metrics import Reranker


@pytest.fixture
def reranker():
    return Reranker()


@pytest.fixture
def candidates():
    return [
        ["ho", "o", "", "o", "", "", "Huh.", "Huh.", "All right.", "Oh", "Okay."],
        ["Do I come off?", "Do I come off???", "Do 1 come off?", "Do I come off?!", "Do I come off?!?!"],
    ]


def test_standardize_metric_name(reranker):
    assert reranker._standardize_metric_name("chrf++") == "get_score_chrf_plus_plus"
    assert reranker._standardize_metric_name("chrf") == "get_score_chrf"
    assert reranker._standardize_metric_name("mer") == "get_score_mer"
    assert reranker._standardize_metric_name("ter") == "get_score_ter"
    assert reranker._standardize_metric_name("wer") == "get_score_wer"
    assert reranker._standardize_metric_name("wip") == "get_score_wip"
    assert reranker._standardize_metric_name("wil") == "get_score_wil"


def test_calculate_accumulated_scores(reranker, candidates):
    scores = reranker._calculate_accumulated_scores(candidates[0], "get_score_chrf_plus_plus")
    assert isinstance(scores, list)
    assert all(isinstance(score, float) for score in scores)


def test_select_best_hypothesis_max(reranker, candidates):
    scores = [0.1, 0.2, 0.3, 0.4]
    best_hypothesis = reranker._select_best_hypothesis_max(candidates[0], scores)
    assert best_hypothesis == candidates[0][3]


def test_select_best_hypothesis_min(reranker, candidates):
    scores = [0.4, 0.3, 0.2, 0.1]
    best_hypothesis = reranker._select_best_hypothesis_min(candidates[0], scores)
    assert best_hypothesis == candidates[0][3]


def test_rerank_chrf(reranker, candidates):
    reranked_candidates = reranker.rerank(candidates, "chrf")
    assert isinstance(reranked_candidates, list)
    assert len(reranked_candidates) == len(candidates)


def test_rerank_chrf_plus_plus(reranker, candidates):
    reranked_candidates = reranker.rerank(candidates, "chrf++")
    assert isinstance(reranked_candidates, list)
    assert len(reranked_candidates) == len(candidates)


def test_rerank_wip(reranker, candidates):
    reranked_candidates = reranker.rerank(candidates, "wip")
    assert isinstance(reranked_candidates, list)
    assert len(reranked_candidates) == len(candidates)


def test_rerank_ter(reranker, candidates):
    reranked_candidates = reranker.rerank(candidates, "ter")
    assert isinstance(reranked_candidates, list)
    assert len(reranked_candidates) == len(candidates)


def test_rerank_wer(reranker, candidates):
    reranked_candidates = reranker.rerank(candidates, "wer")
    assert isinstance(reranked_candidates, list)
    assert len(reranked_candidates) == len(candidates)


def test_rerank_mer(reranker, candidates):
    reranked_candidates = reranker.rerank(candidates, "mer")
    assert isinstance(reranked_candidates, list)
    assert len(reranked_candidates) == len(candidates)


def test_rerank_wil(reranker, candidates):
    reranked_candidates = reranker.rerank(candidates, "wil")
    assert isinstance(reranked_candidates, list)
    assert len(reranked_candidates) == len(candidates)
