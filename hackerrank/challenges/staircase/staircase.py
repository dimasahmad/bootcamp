# staircase
# https://www.hackerrank.com/challenges/staircase/problem

def staircase(n: int):
    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * i)
