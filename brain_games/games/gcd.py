"""GCD check."""


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
