"""Functions for even game."""


import random

import prompt

RIGHT_ANSWER_NEEDED = 3
RANDOM_CALC_MAX = 20
RANDOM_GCD_MAX = 50


def welcome_user():
    """Return user name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def ckeck_answer(user_answer, right_answer, user_name):
    """Check user answer."""
    if user_answer != right_answer:
        print(
            "'{0}' is wrong answer ;(. ".format(user_answer)
            + "Correct answer was '{0}'".format(right_answer)
        )
>>>>>>> refs/remotes/origin/main
        print("Let's try again, {0}!".format(user_name))
        return False
    print('Correct!')
    return True


def is_even(num):
    """Check for even."""
    return num % 2 == 0


def even_game(user_name):
    """Check user knowlenge about even numbers."""
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_answer_count = 0
    while right_answer_count < RIGHT_ANSWER_NEEDED:
        random_number = random.randint(0, 100)
        if is_even(random_number):
            right_answer = 'yes'
        else:
            right_answer = 'no'
        print('Question: {0}'.format(random_number))
        user_answer = prompt.string('Your answer: ')
        if ckeck_answer(user_answer, right_answer, user_name):
            right_answer_count += 1
        else:
            return
    print('Congratulations, {0}!'.format(user_name))


def get_result(num1, num2, operation):
    """Find result of math operation."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2


def calc_game(user_name):
    """Check user knowlenge in simple math."""
    print('What is the result of the expression?')
    right_answer_count = 0
    while right_answer_count < RIGHT_ANSWER_NEEDED:
        rndm_num1 = random.randint(0, RANDOM_CALC_MAX)
        rndm_num2 = random.randint(0, RANDOM_CALC_MAX)
        rndm_oper = random.choice(['+', '-', '*'])
        right_answer = str(get_result(rndm_num1, rndm_num2, rndm_oper))
        print('Question: {0} {1} {2}'.format(rndm_num1, rndm_oper, rndm_num2))
        user_answer = prompt.string('Your answer: ')
        if ckeck_answer(user_answer, right_answer, user_name):
            right_answer_count += 1
        else:
            return
    print('Congratulations, {0}!'.format(user_name))


def find_gcd(num1, num2):
    """Find GCD."""
    if num1 == num2:
        return num1
    if num1 > num2:
        gcd = num2
    else:
        gcd = num1
    while gcd != 1:
        if num1 % gcd == 0 and num2 % gcd == 0:
            break
        gcd -= 1
    return gcd


def gcd_game(user_name):
    """Check user knowlenge in simple math."""
    print('Find the greatest common divisor of given numbers.')
    right_answer_count = 0
    while right_answer_count < RIGHT_ANSWER_NEEDED:
        random_number1 = random.randint(1, RANDOM_GCD_MAX)
        random_number2 = random.randint(1, RANDOM_GCD_MAX)
        right_answer = str(find_gcd(random_number1, random_number2))
        print('Question: {0} {1}'.format(random_number1, random_number2))
        user_answer = prompt.string('Your answer: ')
        if ckeck_answer(user_answer, right_answer, user_name):
            right_answer_count += 1
        else:
            return
    print('Congratulations, {0}!'.format(user_name))


def make_progression():
    """Make progression with random length start and step."""
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    numbers = []
    for i in range(length):
        numbers.append(start + step * i)
    return numbers


def prog_game(user_name):
    """Check user knowlenge in understanding progression."""
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
        if ckeck_answer(user_answer, right_answer, user_name):
            right_answer_count += 1
        else:
            return
    print('Congratulations, {0}!'.format(user_name))


def is_prime(num):
    """Check num for prime."""
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


def prime_game(user_name):
    """Check user knowlenge in prime numbers."""
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    right_answer_count = 0
    while right_answer_count < RIGHT_ANSWER_NEEDED:
        random_number = random.randint(1, 100)
        if is_prime(random_number):
            right_answer = 'yes'
        else:
            right_answer = 'no'
        print('Question: {0}'.format(random_number))
        user_answer = prompt.string('Your answer: ')
        if ckeck_answer(user_answer, right_answer, user_name):
            right_answer_count += 1
        else:
            return
    print('Congratulations, {0}!'.format(user_name))
