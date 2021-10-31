# utopian tree
# https://www.hackerrank.com/challenges/utopian-tree/problem

def utopian_tree(n: int) -> int:
    """Determine how tall the tree after `n` growth cycle.

    Args:
        n (int): the number of growth cycles to simulate

    Returns:
        int: the height of the tree after the given number of cycles
    """

    height: int = 1

    for i in range(1, n + 1):
        if i % 2 == 1:
            height *= 2
        else:
            height += 1

    return height
    