# drawing book
# https://www.hackerrank.com/challenges/drawing-book/problem

def page_count(n: int, p: int) -> int:
    """Determine minimum number of pages that must be turned in order to arrive at a page.

    Args:
        n (int): the number of pages in the book
        p (int): the page number to turn to

    Returns:
        int: the minimum number of pages to turn
    """

    front = p // 2
    back = n // 2 - p // 2

    return min([front, back])
