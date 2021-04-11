#!/usr/bin/env python
"""Calc programm."""

import random

import prompt
from brain_games.games.calc import get_result
from brain_games.games_module import (
    RIGHT_ANSWER_NEEDED,
    check_answer,
    welcome_user,
)

RANDOM_CALC_MAX = 20


def main():
    """Check user knowlenge in simple math."""
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    print('What is the result of the expression?')
    right_answer_count = 0
    while right_answer_count < RIGHT_ANSWER_NEEDED:
        rndm_num1 = random.randint(0, RANDOM_CALC_MAX)
        rndm_num2 = random.randint(0, RANDOM_CALC_MAX)
        rndm_oper = random.choice(['+', '-', '*'])
        right_answer = str(get_result(rndm_num1, rndm_num2, rndm_oper))
        print('Question: {0} {1} {2}'.format(rndm_num1, rndm_oper, rndm_num2))
        user_answer = prompt.string('Your answer: ')
        if check_answer(user_answer, right_answer, user_name):
            right_answer_count += 1
        else:
            return
    print('Congratulations, {0}!'.format(user_name))


if __name__ == '__main__':
    main()
