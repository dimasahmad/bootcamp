# factorial
# https://edabit.com/challenge/FF6kYPHdAcJnoosr5

def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print('factorial(2):\n\t{}'.format(factorial(2)))
print('factorial(6):\n\t{}'.format(factorial(6)))
print('factorial(3):\n\t{}'.format(factorial(3)))
print('factorial(12):\n\t{}'.format(factorial(12)))
print('factorial(5):\n\t{}'.format(factorial(5)))