# find digits
# https://www.hackerrank.com/challenges/find-digits/problem

def find_digits(n: int) -> int:
    """Count the number of divisors for each digit that makes up the integer.

    Args:
        n (int): value to analyze

    Returns:
        int: number of digits in `n` that are divisors of `n`
    """

    return len([int(x) for x in str(n) if int(x) != 0 and n % int(x) == 0])
