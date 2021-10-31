# strong password
# https://www.hackerrank.com/challenges/strong-password/problem

import re


def minimum_number(password: str) -> int:
    """Find the minimum number of characters to add to make password strong.
    
    Args:
        password (str): password to test
    
    Returns:
        int: minimum number of characters to add
    """

    count = len([
        pattern
        for pattern in ['[a-z]', '[A-Z]', '[0-9]', '[!@#$%^&*()\-+]']
        if not re.findall(pattern, password)
    ])

    return max(count, 6 - len(password))