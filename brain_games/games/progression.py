"""Make progression."""

import random

PROG_LENGTH_MIN = 5
PROG_LENGTH_MAX = 10
PROG_START_MIN = 1
PROG_START_MAX = 10
PROG_STEP_MIN = 1
PROG_STEP_MAX = 5
RULE = 'What number is missing in the progression?'


def make_progression(length, start, step):
    """Make progression with random length start and step."""
    return [str(start + step * i) for i in range(length)]


def generate_round():
    """Progression game core."""
    length = random.randint(PROG_LENGTH_MIN, PROG_LENGTH_MAX)
    start = random.randint(PROG_START_MIN, PROG_START_MAX)
    step = random.randint(PROG_STEP_MIN, PROG_STEP_MAX)
    progression = make_progression(length, start, step)
    empty = random.randint(0, len(progression) - 1)
    right_answer = str(progression[empty])
    progression[empty] = '..'
    question = ' '.join(progression)
    return question, right_answer
