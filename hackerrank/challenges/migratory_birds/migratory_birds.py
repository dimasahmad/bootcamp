# migratory birds
# https://www.hackerrank.com/challenges/migratory-birds/problem

def migratory_birds(birds: list[int]) -> int:
    """Determine the most frequently sighted bird type

    Args:
        birds (list[int]): ids of birds sighted

    Returns:
        int: lowest id of the most frequently sighted bird type
    """

    # counter for each 5 birds
    birds_count: list[int] = [0] * 5 # [0, 0, 0, 0, 0]

    for id in birds:
        birds_count[id - 1] += 1

    most: int = max(birds_count)
    most_id: int = birds_count.index(most) + 1

    return most_id
