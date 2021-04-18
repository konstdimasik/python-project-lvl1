"""GCD check."""

import random

RANDOM_GCD_MAX = 50
RULES = 'Find the greatest common divisor of given numbers.'


def find_gcd(num1, num2):
    """Find GCD."""
    if num1 == num2:
        return num1
    gcd = min(num1, num2)
    while gcd != 1:
        if num1 % gcd == 0 and num2 % gcd == 0:
            break
        gcd -= 1
    return gcd


def generate_level():
    """GCD game core."""
    random_number1 = random.randint(1, RANDOM_GCD_MAX)
    random_number2 = random.randint(1, RANDOM_GCD_MAX)
    right_answer = str(find_gcd(random_number1, random_number2))
    question = 'Question: {0} {1}'.format(random_number1, random_number2)
    return question, right_answer
