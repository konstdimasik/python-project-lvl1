"""Make progression."""

import random

RULES = 'What number is missing in the progression?'


def make_progression():
    """Make progression with random length start and step."""
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    numbers = []
    for i in range(length):
        numbers.append(start + step * i)
    return numbers


def generate_level():
    """Progression game core."""
    progression = make_progression()
    random_position = random.randint(0, len(progression) - 1)
    right_answer = str(progression[random_position])
    question = 'Question: '
    for i, num in enumerate(progression):
        if i == random_position:
            question += '.. '
        else:
            question += '{0} '.format(num)
    return question, right_answer
