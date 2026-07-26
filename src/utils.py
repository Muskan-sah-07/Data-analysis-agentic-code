"""Utility functions for examples."""
from typing import List


def calculate_mean(numbers: List[float]) -> float:
    """Return the arithmetic mean of a non-empty list of numbers.

    Raises ValueError if the input list is empty.
    """
    if not numbers:
        raise ValueError("numbers must be non-empty")
    return sum(numbers) / len(numbers)
