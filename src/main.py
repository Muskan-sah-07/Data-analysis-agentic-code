"""Example CLI entrypoint for the Data Analytics Agent starter."""
from __future__ import annotations

import argparse
from typing import List

from .utils import calculate_mean, calculate_median, calculate_sum


def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Example Data Analytics Agent CLI")
    parser.add_argument(
        "--numbers",
        nargs="*",
        type=float,
        help="List of numbers to compute descriptive statistics for",
    )
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> None:
    args = parse_args(argv)
    if args.numbers:
        total = calculate_sum(args.numbers)
        mean = calculate_mean(args.numbers)
        median = calculate_median(args.numbers)
        print(f"Sum of {args.numbers} is {total}")
        print(f"Mean of {args.numbers} is {mean}")
        print(f"Median of {args.numbers} is {median}")
    else:
        print("Hello from Data Analytics Agent! Provide --numbers to compute statistics.")
        sample = [1, 2, 3, 4, 5]
        print(f"Sample sum for {sample} is {calculate_sum(sample)}")
        print(f"Sample mean for {sample} is {calculate_mean(sample)}")
        print(f"Sample median for {sample} is {calculate_median(sample)}")


if __name__ == "__main__":
    main()
