"""Utility functions for examples."""
from typing import List


def calculate_sum(numbers: List[float]) -> float:
    """Return the sum of a non-empty list of numbers."""
    if not numbers:
        raise ValueError("numbers must be non-empty")
    return sum(numbers)


def calculate_mean(numbers: List[float]) -> float:
    """Return the arithmetic mean of a non-empty list of numbers.

    Raises ValueError if the input list is empty.
    """
    if not numbers:
        raise ValueError("numbers must be non-empty")
    return sum(numbers) / len(numbers)


def calculate_median(numbers: List[float]) -> float:
    """Return the median of a non-empty list of numbers."""
    if not numbers:
        raise ValueError("numbers must be non-empty")
    sorted_numbers = sorted(numbers)
    mid = len(sorted_numbers) // 2
    if len(sorted_numbers) % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]
