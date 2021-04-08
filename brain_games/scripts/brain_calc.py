#!/usr/bin/env python
"""Calc programm."""


from brain_games.games_module import calc_game, welcome_user


def main():
    """Make a user intreface."""
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    calc_game(user_name)


if __name__ == '__main__':
    main()
