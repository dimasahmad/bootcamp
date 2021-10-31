# compare the triplets
# https://www.hackerrank.com/challenges/compare-the-triplets/problem

def compare_triplets(a: list[int], b: list[int]) -> list[int]:
    a_points: int = 0
    b_points: int = 0

    for i in range(3):
        a_points += a[i] > b[i]
        b_points += b[i] > a[i]

    return [a_points, b_points]
