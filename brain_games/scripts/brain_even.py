#!/usr/bin/env python
"""Even programm."""

from brain_games.game_engine import run
from brain_games.games import even


def main():
    """Check user knowlenge about even numbers."""
    run(even)


if __name__ == '__main__':
    main()
