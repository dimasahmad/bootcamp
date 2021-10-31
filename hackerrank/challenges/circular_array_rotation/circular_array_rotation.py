# circular array notation
# https://www.hackerrank.com/challenges/circular-array-rotation/problem

def circular_array_rotation(a: list[int], k: int, queries: list[int]) -> list[int]:
    """Perform a number of right circular rotations and
    return the values of the elements at the given indices.

    Args:
        a (list[int]): array to rotate
        k (int): rotation count
        queries (list[int]): indices to report

    Returns:
        list[int]: values in the rotated `a` as requested in `m`
    """

    # rotate right `k` times
    k = k % len(a)
    a = a[len(a) - k:] + a[:len(a) - k]

    return [a[q] for q in queries]
