# beautiful days at the movie
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

def beautiful_days(i: int, j: int, k: int) -> int:
    """Determine the number of days in the range that are beautiful.

    Beautiful numbers are defined as numbers where `|i - reverse(i)|`
    is evenly divisible by `k`. If a day's value is a beautiful number,
    it is a beautiful day. Return the number of beautiful days in the range.

    Args:
        i (int): starting day
        j (int): ending day
        k (int): divisor

    Returns:
        int: number of beautiful days in the range
    """

    return len([x for x in range(i, j + 1) if abs(x - int(str(x)[::-1])) % k == 0])
