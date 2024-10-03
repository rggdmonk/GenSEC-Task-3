import pytest

from gensec.metrics import MetricsHigherIsBetter, MetricsLowerIsBetter


class TestMetricsLowerIsBetter:
    @pytest.fixture
    def metrics(self):
        return MetricsLowerIsBetter()

    def test_get_score_ter(self, metrics):
        hypothesis = "This is a test"
        reference = ["This is a test"]
        score = metrics.get_score_ter(hypothesis, reference)
        assert isinstance(score, float)
        assert score == 0.0

    def test_get_score_wer(self, metrics):
        hypothesis = "This is a test"
        reference = "This is a test"
        score = metrics.get_score_wer(hypothesis, reference)
        assert isinstance(score, float)
        assert score == 0.0

    def test_get_score_mer(self, metrics):
        hypothesis = "This is a test"
        reference = "This is a test"
        score = metrics.get_score_mer(hypothesis, reference)
        assert isinstance(score, float)
        assert score == 0.0

    def test_get_score_wil(self, metrics):
        hypothesis = "This is a test"
        reference = "This is a test"
        score = metrics.get_score_wil(hypothesis, reference)
        assert isinstance(score, float)
        assert score == 0.0


class TestMetricsHigherIsBetter:
    @pytest.fixture
    def metrics(self):
        return MetricsHigherIsBetter()

    def test_get_score_chrf(self, metrics):
        hypothesis = "This is a test"
        reference = ["This is a test"]
        score = metrics.get_score_chrf(hypothesis, reference)
        assert isinstance(score, float)
        assert score == 100.0

    def test_get_score_chrf_plus_plus(self, metrics):
        hypothesis = "This is a test"
        reference = ["This is a test"]
        score = metrics.get_score_chrf_plus_plus(hypothesis, reference)
        assert isinstance(score, float)
        assert score == 100.0

    def test_get_score_wip(self, metrics):
        hypothesis = "This is a test"
        reference = "This is a test"
        score = metrics.get_score_wip(hypothesis, reference)
        assert isinstance(score, float)
        assert score == 1.0
