#!/usr/bin/env python
"""Prime programm."""

from brain_games.game_engine import run
from brain_games.games import prime


def main():
    """Check user knowlenge in prime numbers."""
    run(prime)


if __name__ == '__main__':
    main()
