#!/usr/bin/env python
"""Calc programm."""

from brain_games.games import calc
from brain_games.games_module import engine


def main():
    """Check user knowlenge in simple math."""
    engine(calc)


if __name__ == '__main__':
    main()
