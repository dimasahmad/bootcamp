# simple array sum
# https://www.hackerrank.com/challenges/simple-array-sum/problem

def simple_array_sum(ar: list[int]) -> int:
    ar_sum = 0
    for n in ar:
        ar_sum += n

    return ar_sum
