"""Prime check."""


def is_prime(num):
    """Check num for prime."""
    if num % 2 == 0:
        return num == 2
    divider = 3
    while divider * divider <= num and num % divider != 0:
        divider += 2
    return divider * divider > num
