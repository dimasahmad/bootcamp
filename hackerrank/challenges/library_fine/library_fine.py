# library fine
# https://www.hackerrank.com/challenges/library-fine/problem


def library_fine(d1: int, m1: int, y1: int, d2: int, m2: int, y2: int) -> int:
    """Calculates library fines.
    
    Args:
        d1 (int): returned day
        m1 (int): returned month
        y1 (int): returned year
        d2 (int): due day
        m2 (int): due month
        y2 (int): due year

    Returns:
        int: amount of the fine or 0 if there is none
    """

    if y1 <= y2 and m1 == m2 and d1 > d2:
        return (d1 - d2) * 15

    if y1 == y2 and m1 > m2:
        return (m1 - m2) * 500

    if y1 > y2:
        return 10000

    return 0