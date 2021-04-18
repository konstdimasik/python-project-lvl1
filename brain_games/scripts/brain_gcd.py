#!/usr/bin/env python
"""GCD programm."""

from brain_games.game_engine import run
from brain_games.games import gcd


def main():
    """Check user knowlenge in simple math."""
    run(gcd)


if __name__ == '__main__':
    main()
