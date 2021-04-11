#!/usr/bin/env python
"""GCD programm."""

import random

import prompt
from brain_games.games.gcd import find_gcd
from brain_games.games_module import (
    RIGHT_ANSWER_NEEDED,
    check_answer,
    welcome_user,
)

RANDOM_GCD_MAX = 50


def main():
    """Check user knowlenge in simple math."""
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    right_answer_count = 0
    while right_answer_count < RIGHT_ANSWER_NEEDED:
        random_number1 = random.randint(1, RANDOM_GCD_MAX)
        random_number2 = random.randint(1, RANDOM_GCD_MAX)
        right_answer = str(find_gcd(random_number1, random_number2))
        print('Question: {0} {1}'.format(random_number1, random_number2))
        user_answer = prompt.string('Your answer: ')
        if check_answer(user_answer, right_answer, user_name):
            right_answer_count += 1
        else:
            return
    print('Congratulations, {0}!'.format(user_name))


if __name__ == '__main__':
    main()
