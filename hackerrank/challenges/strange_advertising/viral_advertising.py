# viral advertising
# https://www.hackerrank.com/challenges/strange-advertising/problem

def viral_advertising(n: int) -> int:
    """Determine how many people have liked the ad by the end of a given day.

    Args: 
        n (int): day number to report

    Returns:
        int: cumulative likes at that day
    """

    likes: int = 5 // 2
    cumulative: int = likes

    for x in range(1, n):
        likes = (likes * 3) // 2
        cumulative += likes

    return cumulative
