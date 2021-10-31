# sales by match
# https://www.hackerrank.com/challenges/sock-merchant/problem

def sock_merchant(socks: list[int]) -> int:
    """Determine how many pairs of socks with matching colors.

    Given an array of integers representing the color of each sock,
    determine how many pairs of socks with matching colors there are.

    Args:
        socks (int): color_id of each socks

    Returns:
        int: pairs of socks
    """

    socks_pile: dict[int, int] = {} # {color_id: count}

    for color_id in socks:
        if color_id not in socks_pile:
            socks_pile[color_id] = 1
        else:
            socks_pile[color_id] += 1

    pairs: int = 0

    for color_id in socks_pile:
        pairs += socks_pile[color_id] // 2
    
    return pairs
