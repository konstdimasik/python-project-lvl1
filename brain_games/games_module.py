"""Functions for even game."""

import prompt

RIGHT_ANSWER_NEEDED = 3


def welcome_user():
    """Return user name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def check_answer(user_answer, right_answer, user_name):
    """Check user answer."""
    if user_answer != right_answer:
        print(
            "'{0}' is wrong answer ;(. ".format(user_answer)
            + "Correct answer was '{0}'".format(right_answer)
        )
        print("Let's try again, {0}!".format(user_name))
        return False
    print('Correct!')
    return True
