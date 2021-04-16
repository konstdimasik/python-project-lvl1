"""Functions for even game."""

import prompt

RIGHT_ANSWER_NEEDED = 3


def welcome_user():
    """Return user name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def check_answer(user_answer, right_answer):
    """Check user answer."""
    if user_answer != right_answer:
        print(
            "'{0}' is wrong answer ;(. ".format(user_answer)
            + "Correct answer was '{0}'".format(right_answer)
        )
        return False
    print('Correct!')
    return True


def engine(game):
    """Engine for all games."""
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    print(game.RULES)
    for _ in range(RIGHT_ANSWER_NEEDED):
        question, right_answer = game.generate_level()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if not check_answer(user_answer, right_answer):
            print("Let's try again, {0}!".format(user_name))
            return
    print('Congratulations, {0}!'.format(user_name))
