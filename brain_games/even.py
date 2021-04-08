"""Functions for even game."""


import random

import prompt


def welcome_user():
    """Return user name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def even_game(user_name):
    """Check "user_name" knowlenge about even numbers."""
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_answer_count = 0
    while right_answer_count < 3:
        random_number = random.randint(0, 100)
        if random_number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        print('Question: {0}'.format(random_number))
        user_answer = prompt.string('Your answer: ')
        if user_answer != right_answer:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(user_answer, right_answer))
            print("Let's try again, {0}!".format(user_name))
            right_answer_count = 0
            continue
        print('Correct!')
        right_answer_count += 1
    print('Congratulations, {0}!'.format(user_name))
