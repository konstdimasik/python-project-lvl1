"""Functions for even game."""

import prompt

RIGHT_ANSWER_NEEDED = 3


def run(game):
    """Engine for all games."""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    print(game.RULES)
    for _ in range(RIGHT_ANSWER_NEEDED):
        question, right_answer = game.generate_level()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer != right_answer:
            print(
                "'{0}' is wrong answer ;(. ".format(user_answer)
                + "Correct answer was '{0}'".format(right_answer)
            )
            print("Let's try again, {0}!".format(user_name))
            return
        print('Correct!')
    print('Congratulations, {0}!'.format(user_name))
