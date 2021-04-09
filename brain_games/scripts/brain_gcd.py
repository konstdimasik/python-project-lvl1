#!/usr/bin/env python
"""GCD programm."""


from brain_games.games_module import gcd_game, welcome_user


def main():
    """Make a user intreface."""
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    gcd_game(user_name)


if __name__ == '__main__':
    main()
