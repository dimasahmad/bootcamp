# between two sets
# https://www.hackerrank.com/challenges/between-two-sets/problem

def get_total_x(a: list[int], b: list[int]) -> int:
    """Determine how many numbers that are between two sets

    Determine all integers that satisfy the following two conditions:
    - The elements of the first array are all factors of the integer being considered
    - The integer being considered is a factor of all elements of the second array

    Args:
        a (list[int]): fators of the integers being considered
        b (list[int]): numbers that has factors of the integers being considered

    Returns:
        int: the number of integers that are between the sets
    """

    a_max: int = max(a)
    b_min: int = min(b)

    # multiples of a_max
    numbers: list[int] = []
    for x in range(1, b_min // a_max + 1):
        numbers.append(x * a_max)

    # calculate numbers that
    # - each a[] is a factor of the number
    # - the number is factor of each b[]
    divisible: list[int] = []
    for test_number in numbers:
        test: bool = True

        for test_a in a:
            test = test and (test_number % test_a == 0)
        for test_b in b:
            test = test and (test_b % test_number == 0)

        if test:
            divisible.append(test_number)

    return len(divisible)
