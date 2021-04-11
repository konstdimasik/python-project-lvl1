"""Make progression."""

import random


def make_progression():
    """Make progression with random length start and step."""
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    numbers = []
    for i in range(length):
        numbers.append(start + step * i)
    return numbers
