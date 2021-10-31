def accept_integer(func):
    """Convert function parameter from integer to string"""
    def new_func(s: int | str):
        if isinstance(s, int):
            s = str(s)
        return func(s)

    return new_func


@accept_integer
def append_world(string: str) -> str:
    """Append ` world!` to a string."""
    return string + " world!"


@accept_integer
def prepend_hello(string: str) -> str:
    """Prepend `Hello ` to a string."""
    return "Hello " + string


@accept_integer
def make_palindrome(string: str) -> str:
    """Makes a palindromic mirror of a string."""
    return string + string[::-1]


if __name__ == "__main__":
    print(__name__)
    print(append_world(1))