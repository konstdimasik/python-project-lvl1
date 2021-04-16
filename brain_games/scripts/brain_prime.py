#!/usr/bin/env python
"""Prime programm."""

from brain_games.games import prime
from brain_games.games_module import engine


def main():
    """Check user knowlenge in prime numbers."""
    engine(prime)


if __name__ == '__main__':
    main()
