import pytest

from gensec.naive_heuristics import NaiveHeuristics


@pytest.fixture
def naive_heuristics():
    return NaiveHeuristics(seed=42)


def test_count_punctuation_chars(naive_heuristics):
    assert naive_heuristics.count_punctuation_chars("Hello, world!") == 2
    assert naive_heuristics.count_punctuation_chars("No punctuation") == 0


def test_naive_selection_longest(naive_heuristics):
    all_candidates = [["short", "longer", "longest"]]
    assert naive_heuristics.naive_selection(all_candidates, "longest") == ["longest"]


def test_naive_selection_shortest(naive_heuristics):
    all_candidates = [["short", "longer", "longest"]]
    assert naive_heuristics.naive_selection(all_candidates, "shortest") == ["short"]


def test_naive_selection_most_punctuation(naive_heuristics):
    all_candidates = [["no punctuation", "one, punctuation", "two, punctuations!"]]
    assert naive_heuristics.naive_selection(all_candidates, "most_punctuation") == ["two, punctuations!"]


def test_naive_selection_least_punctuation(naive_heuristics):
    all_candidates = [["no punctuation", "one, punctuation", "two, punctuations!"]]
    assert naive_heuristics.naive_selection(all_candidates, "least_punctuation") == ["no punctuation"]


def test_naive_selection_random(naive_heuristics):
    all_candidates = [["option1", "option2", "option3"]]
    result = naive_heuristics.naive_selection(all_candidates, "random")
    assert result[0] in ["option1", "option2", "option3"]


def test_naive_selection_longest_and_most_punctuation(naive_heuristics):
    all_candidates = [["short", "longer,", "longest!"]]
    assert naive_heuristics.naive_selection(all_candidates, "longest_and_most_punctuation") == ["longest!"]


def test_naive_selection_shortest_and_least_punctuation(naive_heuristics):
    all_candidates = [["short", "longer,", "longest!"]]
    assert naive_heuristics.naive_selection(all_candidates, "shortest_and_least_punctuation") == ["short"]


def test_naive_selection_longest_and_least_punctuation(naive_heuristics):
    all_candidates = [["short", "longer,", "longest!"]]
    assert naive_heuristics.naive_selection(all_candidates, "longest_and_least_punctuation") == ["longest!"]


def test_naive_selection_shortest_and_most_punctuation(naive_heuristics):
    all_candidates = [["short", "longer,", "longest!"]]
    assert naive_heuristics.naive_selection(all_candidates, "shortest_and_most_punctuation") == ["short"]


def test_naive_selection_invalid_metric(naive_heuristics):
    all_candidates = [["short", "longer", "longest"]]
    with pytest.raises(NotImplementedError):
        naive_heuristics.naive_selection(all_candidates, "invalid_metric")


def test_naive_selection_empty_input(naive_heuristics):
    with pytest.raises(AssertionError):
        naive_heuristics.naive_selection([], "longest")


def test_naive_selection_empty_inner_list(naive_heuristics):
    with pytest.raises(AssertionError):
        naive_heuristics.naive_selection([[]], "longest")
