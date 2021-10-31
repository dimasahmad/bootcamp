# repeated string
# https://www.hackerrank.com/challenges/repeated-string/problem

def repeated_string(s: str, n: int) -> int:
    """Find and print the number of letter a's in the first `n` letters of the infinite string `s`
    
    Args:
        s (str): string to repeat
        n (int): number of characters to consider

    Returns:
        int: frequency of `a` in the substring
    """

    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")