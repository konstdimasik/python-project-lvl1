#!/usr/bin/env python
"""Progression programm."""

import random

import prompt
from brain_games.games.progression import make_progression
from brain_games.games_module import (
    RIGHT_ANSWER_NEEDED,
    check_answer,
    welcome_user,
)


def main():
    """Check user knowlenge in understanding progression."""
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    print('What number is missing in the progression?')
    right_answer_count = 0
    while right_answer_count < RIGHT_ANSWER_NEEDED:
        progression = make_progression()
        random_position = random.randint(0, len(progression) - 1)
        right_answer = str(progression[random_position])
        print('Question: ', end='')
        for i, num in enumerate(progression):
            if i == random_position:
                print('.. ', end='')
            else:
                print('{0} '.format(num), end='')
        user_answer = prompt.string('\nYour answer: ')
        if check_answer(user_answer, right_answer, user_name):
            right_answer_count += 1
        else:
            return
    print('Congratulations, {0}!'.format(user_name))


if __name__ == '__main__':
    main()
