# counting valleys
# https://www.hackerrank.com/challenges/counting-valleys/problem

def counting_valleys(steps: int, path: str) -> int:
    """Find the number of valleys walked through

    Args:
        steps (int): the number of steps on the hike
        path (str): a string describing the path

    Returns:
        int: the number of valleys traversed
    """

    elevation: int = 0
    valleys: int = 0

    for step in path:
        elevation += 1 if step == "U" else -1

        if step == "U" and elevation == 0:
            valleys += 1

    return valleys
