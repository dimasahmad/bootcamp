# mini-max sum
# https://www.hackerrank.com/challenges/mini-max-sum/problem

def mini_max_sum(arr: list[int]):
    mini = sum(arr) - max(arr)
    maxi = sum(arr) - min(arr)
    print(mini, maxi)
