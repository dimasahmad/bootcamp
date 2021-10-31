# cylinder of water mass
# https://edabit.com/challenge/iP4ixkQffELyHvHi5


import math


def weight(radius: int, height: int) -> int:
    # calculate the volume of the cylinder
    volume: int = math.pi * radius ** 2 * height  # in cm cubic

    # convert water volume into mass
    mass: int = volume / 1000  # in dm cubic (1 dm cubic = 1L of water = 1Kg)

    return round(mass, 2)


print('weight(4, 10):\n\t{}'.format(weight(4, 10)))
print('weight(30, 60):\n\t{}'.format(weight(30, 60)))
print('weight(15, 10):\n\t{}'.format(weight(15, 10)))
print('weight(20, 40):\n\t{}'.format(weight(20, 40)))
print('weight(100, 30):\n\t{}'.format(weight(100, 30)))
print('weight(200, 300):\n\t{}'.format(weight(200, 300)))
print('weight(15, 23):\n\t{}'.format(weight(15, 23)))
print('weight(22, 44):\n\t{}'.format(weight(22, 44)))
