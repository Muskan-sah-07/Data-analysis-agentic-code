"""Example CLI entrypoint for the Data Analytics Agent starter."""
from __future__ import annotations

import argparse
from typing import List

from .utils import calculate_mean


def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Example Data Analytics Agent CLI")
    parser.add_argument(
        "--numbers",
        nargs="*",
        type=float,
        help="List of numbers to compute mean for",
    )
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> None:
    args = parse_args(argv)
    if args.numbers:
        mean = calculate_mean(args.numbers)
        print(f"Mean of {args.numbers} is {mean}")
    else:
        print("Hello from Data Analytics Agent! Provide --numbers to compute a mean.")
        sample = [1, 2, 3, 4, 5]
        print(f"Sample mean for {sample} is {calculate_mean(sample)}")


if __name__ == "__main__":
    main()
