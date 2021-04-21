"""Even check."""

import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    """Check for even."""
    return num % 2 == 0


def generate_round():
    """Even game core."""
    random_number = random.randint(1, 100)
    if is_even(random_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = '{0}'.format(random_number)
    return question, right_answer
