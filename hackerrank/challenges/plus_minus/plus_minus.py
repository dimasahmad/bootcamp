# plus minus
# https://www.hackerrank.com/challenges/plus-minus/problem

def plus_minus(numbers: list[int]):
    numbers_len = len(numbers)

    positives = 0
    negatives = 0
    zeroes = 0

    for number in numbers:
        positives += number > 0
        negatives += number < 0
        zeroes += number == 0

    print("{:.6f}".format(positives/numbers_len, 6))
    print("{:.6f}".format(negatives/numbers_len, 6))
    print("{:.6f}".format(zeroes/numbers_len, 6))
