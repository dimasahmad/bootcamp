# divisible sum pairs
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

def divisible_sum_pairs(k: int, ar: list[int]):
    """Determine how many sum of pairs that is divisible by an integer

    Determine the number of [i, j] pairs where
    - i < j
    - ar[i] + ar[j] is divisible by k

    Args:
        k (int): 
        ar (list[int]): 

    Returns:
        int: the number of pairs
    """

    divisible: list[list[int]] = []

    for i in range(len(ar) - 1):
        for j in range(i + 1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                divisible.append([i, j])

    return len(divisible)
