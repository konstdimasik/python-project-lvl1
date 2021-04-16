#!/usr/bin/env python
"""Even programm."""

from brain_games.games import even
from brain_games.games_module import engine


def main():
    """Check user knowlenge about even numbers."""
    engine(even)


if __name__ == '__main__':
    main()
