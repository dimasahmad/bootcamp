# sequence_equation
# https://www.hackerrank.com/challenges/permutation-equation/problem

def permutation_equation(p: list[int]) -> list[int]:
    """

    Args:
        p (list[int]): array of integers

    Returns:
        list[int]: values of `y` for all `x` in the arithmetic sequence `1` to `n`
    """

    return [p.index(p.index(x) + 1) + 1 for x in range(1, len(p) + 1)]
