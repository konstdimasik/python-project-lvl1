"""Prime check."""


def is_prime(num):
    """Check num for prime."""
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True
