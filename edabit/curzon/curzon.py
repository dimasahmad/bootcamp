def is_curzon(x: int) -> bool:
    return (2 ** x + 1) % (2 * x + 1) == 0

def curzon(x: int) -> str:
    # return str(2 ** x + 1) + (" is a multiple of " if is_curzon(x) else " is not a multiple of ") + str(2 * x + 1)

    text = str(2 ** x + 1)
    if is_curzon(x):
        text += " is a multiple of "
    else:
        text += " is not a multiple of "
    text += str(2 * x + 1)

    return text

print(is_curzon(5))
print(curzon(5))
print(is_curzon(120))
print(curzon(120))
print(is_curzon(293))
print(curzon(293))

