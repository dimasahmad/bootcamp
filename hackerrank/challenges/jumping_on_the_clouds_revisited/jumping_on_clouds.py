# jumping on the clouds: revisited
# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

def jumping_on_clouds(c: list[int], k: int) -> int:
    """Determine final energy value after the game ends.

    Args:
        c (list[int]): cloud types along the path, `0` cumulus, `1` thunderclouds
        k (int): length of one jump

    Returns:
        int: energy level remaining
    """

    energy: int = 100
    position: int = 0

    while True:
        position = (position + k) % len(c)
        energy -= 1 if c[position] != 1 else 3

        if position == 0:
            break

    return energy
