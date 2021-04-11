#!/usr/bin/env python
"""Even programm."""

import random

import prompt
from brain_games.games.even import is_even
from brain_games.games_module import (
    RIGHT_ANSWER_NEEDED,
    check_answer,
    welcome_user,
)


def main():
    """Check user knowlenge about even numbers."""
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_answer_count = 0
    while right_answer_count < RIGHT_ANSWER_NEEDED:
        random_number = random.randint(1, 100)
        if is_even(random_number):
            right_answer = 'yes'
        else:
            right_answer = 'no'
        print('Question: {0}'.format(random_number))
        user_answer = prompt.string('Your answer: ')
        if check_answer(user_answer, right_answer, user_name):
            right_answer_count += 1
        else:
            return
    print('Congratulations, {0}!'.format(user_name))


if __name__ == '__main__':
    main()
