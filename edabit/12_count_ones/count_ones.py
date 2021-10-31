# count the amount of ones in the binary representation of an integer
# https://edabit.com/challenge/GbyPdqNnp75Wci7Cn


def count_ones(num: int) -> int:
    return bin(num)[2:].count("1")


print('count_ones(12):\n\t{}'.format(count_ones(12)))
print('count_ones(0):\n\t{}'.format(count_ones(0)))
print('count_ones(100):\n\t{}'.format(count_ones(100)))
print('count_ones(101):\n\t{}'.format(count_ones(101)))
print('count_ones(999):\n\t{}'.format(count_ones(999)))
print('count_ones(123456789):\n\t{}'.format(count_ones(123456789)))
print('count_ones(1234567890):\n\t{}'.format(count_ones(1234567890)))
