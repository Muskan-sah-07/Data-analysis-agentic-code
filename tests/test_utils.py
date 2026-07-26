import pytest

from src.utils import calculate_mean, calculate_median, calculate_sum


def test_calculate_mean_simple():
    assert calculate_mean([1, 2, 3]) == pytest.approx(2.0)


def test_calculate_mean_empty():
    with pytest.raises(ValueError):
        calculate_mean([])


def test_calculate_median_simple():
    assert calculate_median([1, 2, 3]) == pytest.approx(2.0)


def test_calculate_sum_simple():
    assert calculate_sum([1, 2, 3]) == pytest.approx(6.0)
