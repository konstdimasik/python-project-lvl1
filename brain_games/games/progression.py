"""Make progression."""

import random

RULES = 'What number is missing in the progression?'


def make_progression():
    """Make progression with random length start and step."""
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(1, 5)
<<<<<<< HEAD
    return [str(start + step * i) for i in range(length)]
=======
    return [start + step * i for i in range(length)]
>>>>>>> refs/remotes/origin/main


def generate_level():
    """Progression game core."""
    progression = make_progression()
    empty = random.randint(0, len(progression) - 1)
    right_answer = str(progression[empty])
    progression[empty] = '..'
    question = ' '.join(progression)
    return question, right_answer
