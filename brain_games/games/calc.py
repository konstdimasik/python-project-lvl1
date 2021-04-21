"""Calculation check."""

import random

RANDOM_CALC_MAX = 20
RULE = 'What is the result of the expression?'


def get_result(num1, num2, operation):
    """Find result of math operation."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2


def generate_round():
    """Calc game core."""
    rndm_num1 = random.randint(0, RANDOM_CALC_MAX)
    rndm_num2 = random.randint(0, RANDOM_CALC_MAX)
    rndm_oper = random.choice(['+', '-', '*'])
    right_answer = str(get_result(rndm_num1, rndm_num2, rndm_oper))
    question = '{0} {1} {2}'.format(rndm_num1, rndm_oper, rndm_num2)
    return question, right_answer
