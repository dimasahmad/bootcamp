# number line jumps
# https://www.hackerrank.com/challenges/kangaroo/problem

def kangaroo(x1: int, v1: int, x2: int, v2: int) -> str:
    """Determine if two kangaroos will meet
    
    Args:
        x1 (int): kangaroo 1 starting position
        v1 (int): kangaroo 1 jumping distance
        x2 (int): kangaroo 2 starting position
        v2 (int): kangaroo 2 jumping distance

    Returns:
        str: "YES" or "NO"
    """

    # kangaroo 1 won't be able to catch up kangaroo 2
    if x2 > x1 and v2 >= v1:
        return "NO"

    # Naive O(n) solution
    #
    # k1 = x1
    # k2 = x2
    # while True:
    #     k1 += v1
    #     k2 += v2
    #     if k1 == k2:
    #         return "YES"

    # Better O(1) solution
    # i = jump
    #
    # x1 + v1 * i == x2 + v2 * i
    # x1 - x2 == v2 * i - v1 * i
    # x1 - x2 == (v2 - v1) * i
    # (x1 - x2) / (v2 - v1) == i
    #
    # they will meet if i jump is an integer, thus
    # (x1 - x2) % (v2 - v1) == 0
    if (x1 - x2) % (v2 - v1) == 0:
        return "YES"
    else:
        return "NO"
