# convert decimal to binary
# https://edabit.com/challenge/2hsyXkzDRewGSPpPE


def dec2bin(number: int) -> str:
    """
    Convert a positive integer into it's binary representation.

    >>> dec2bin(2796202)
    '1010101010101010101010'
    """

    if number < 0:
        raise ValueError("Must be a positive integer")

    # remainder is the digit
    digit = number % 2

    # quotient for next recursion
    next = number // 2

    if number > 1:
        return dec2bin(next) + str(digit)
    else:
        return str(digit)
