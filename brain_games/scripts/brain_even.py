#!/usr/bin/env python
"""Even programm."""


from brain_games.even import even_game, welcome_user


def main():
    """Make a user intreface."""
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    even_game(user_name)


if __name__ == '__main__':
    main()
