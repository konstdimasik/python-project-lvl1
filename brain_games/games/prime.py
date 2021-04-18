"""Prime check."""

import random

MAX_CHECK_NUM = 100
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    """Check num for prime."""
    if num % 2 == 0:
        return num == 2
    divider = 3
    while divider * divider <= num and num % divider != 0:
        divider += 2
    return divider * divider > num


def generate_level():
    """Prime game core."""
    random_number = random.randint(2, MAX_CHECK_NUM)
    if is_prime(random_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = '{0}'.format(random_number)
    return question, right_answer
