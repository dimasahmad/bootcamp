# designer pdf viewer
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

def designer_pdf_viewer(heights: list[int], word: str) -> int:
    """Determine the area of the highlighted word.

    Args:
        heights (list[int]): the heights of each letter
        word (str): string

    Returns:
        int: the size of the highlighted area
    """

    word_heights: list[int] = []
    
    for char in word:
        word_heights.append(heights[ord(char) - ord("a")])

    return max(word_heights) * len(word)
