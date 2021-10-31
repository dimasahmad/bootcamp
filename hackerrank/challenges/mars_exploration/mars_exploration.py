# mars exploration
# https://www.hackerrank.com/challenges/mars-exploration/problem


def mars_exploration(message: str) -> int:
    """Determine how many letters of the `SOS` message have been changed by radiation.
    
    Args:
        message (str): the string as received on Earth

    Returns:
        int: the number of letters changed during transmission
    """

    return sum([
        len([o for o in range(3) if message[s + o:s + o + 1] != "SOS"[o]])
        for s in range(0, len(message), 3)
    ])
