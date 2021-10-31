# save the prisoner
# https://www.hackerrank.com/challenges/save-the-prisoner/problem

def save_the_prisoner(n: int, m: int, s: int) -> int:
    """Determine the chair number occupied by the prisoner who will receive
    an awful tasting candy.
    
    Args:
        n (int): number of prisoners
        m (int): number of sweets
        s (int): chair number to begin passing out sweets from

    Returns:
        int: chair number of the prisoner to warn
    """

    if m > n - s:
        if (s - 1 + m - n) % n != 0:
            return (s - 1 + m - n) % n
        else:
            return n
    else:
        return s - 1 + m
    
    # return (m - (n - s + 1)) % n if (m - (n - s + 1)) % n != 0 else n if m > n - s else s - 1 + m
