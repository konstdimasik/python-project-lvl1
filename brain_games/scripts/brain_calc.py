#!/usr/bin/env python
"""Calc programm."""

from brain_games.game_engine import run
from brain_games.games import calc


def main():
    """Check user knowlenge in simple math."""
    run(calc)


if __name__ == '__main__':
    main()
