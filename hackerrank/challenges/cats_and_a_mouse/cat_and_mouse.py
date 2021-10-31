# cats and a mouse
# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

def cat_and_mouse(x: int, y: int, z: int) -> str:
    """Determine which cat will reach the mouse first

    The mouse does not move and the cats travel at equal speed.
    If both cats reached the mouse at the same time, mouse escaped.

    Args:
        x (int): `Cat A`'s position
        y (int): `Cat B`'s position
        z (int): `Mouse C`'s position

    Returns:
        str: `Cat A`, `Cat B`, or `Mouse C`
    """

    x_z: int = abs(z - x)
    y_z: int = abs(z - y)

    if x_z < y_z:
        return "Cat A"
    elif x_z > y_z:
        return "Cat B"
    else:
        return "Mouse C"
