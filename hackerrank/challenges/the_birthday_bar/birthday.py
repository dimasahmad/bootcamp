# subarray division
# https://www.hackerrank.com/challenges/the-birthday-bar/problem

def birthday(chocobar: list[int], day: int, month: int) -> int:
    """Determine how many ways Lily can devide chocolate

    Lily decides to share a contiguous segment of the bar selected such that:
    - The length of the segment matches Ron's birth month, and,
    - The sum of the integers on the squares is equal to his birth day.

    Args:
        chocobar (list[int]): the numbers on each of the squares of chocolate
        day (int): Ron's birth day
        month (int): Ron's birth month

    Returns:
        int: the number of ways the bar can be devided
    """

    ways: int = 0

    for i in range(len(chocobar)):
        # choco squares is more than what Lily has
        if i + month > len(chocobar):
            break

        squares: list[int] = []

        for j in range(month):
            squares.append(chocobar[i + j])

        if sum(squares) == day:
            ways += 1

    return ways
