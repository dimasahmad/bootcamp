# the hurdle race
# https://www.hackerrank.com/challenges/the-hurdle-race/problem

def hurdle_race(k: int, height: list[int]):
    """Determine how many doses of the potion needs to be able
    to jump all of the hurdles.

    Args:
        k (int): height the character can jump naturally
        height (list[int]): heights of each hurdle

    Returns:
        int: minimum number of doses required, always 0 or more
    """

    h_max: int = 0

    for h in height:
        if h > h_max:
            h_max = h
    
    potion: int = h_max - k
    
    if potion < 0:
        return 0

    return potion