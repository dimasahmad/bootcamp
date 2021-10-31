# forming a magic square
# https://www.hackerrank.com/challenges/magic-square-forming/problem

def forming_magic_square(s: list[list[int]]) -> int:
    """Convert a matrix into a magic square at minimal cost

    Args:
        s (list[list[int]]): a `3 × 3` array of integers

    Returns:
        int: the minimal total cost of converting the input square to a magic square
    """

    # the easiest solution is to calculate the cost with EVERY possible magic squares

    # characteristics of a 3 x 3 magic square
    # 1. must have 5 in the middle
    # 2. each corners has to be an even number
    # 3. each middle edges has to be an odd number

    # 6 1 8 | 8 1 6     2 7 6 | 6 7 2
    # 7 5 3 | 3 5 7     9 5 1 | 1 5 9
    # 2 9 4 | 4 9 2     4 3 8 | 8 3 4
    # -------------     -------------
    # 2 9 4 | 4 9 2     4 3 8 | 8 3 4
    # 7 5 3 | 3 5 7     9 5 1 | 1 5 9
    # 6 1 8 | 8 1 6     2 7 6 | 6 7 2
    magic_square: list[list[int]] = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]

    # we can generate all possible magic squares by rotating and mirroring a magic square
    # resulting in 8 possible different 3 x 3 magic squares
    n: int = 8

    # store cost for each magic squares
    costs: list[int] = [0] * n

    for i in range(n):
        is_even: bool = i % 2 == 0

        # if is_even, calculate the mirror of the matrix
        for j, [a, b, c] in enumerate(magic_square):
            costs[i] += abs(s[0 if is_even else 2][j] - a)
            costs[i] += abs(s[1][j] - b)
            costs[i] += abs(s[2 if is_even else 0][j] - c)

        # rotate matrix 90 degs clockwise
        if is_even:
            s = list(map(
                lambda j: [s[2][j], s[1][j], s[0][j]],
                list(range(3))
            ))

    return min(costs)
