import pytest

from src.utils import calculate_mean


def test_calculate_mean_simple():
    assert calculate_mean([1, 2, 3]) == pytest.approx(2.0)


def test_calculate_mean_empty():
    with pytest.raises(ValueError):
        calculate_mean([])
