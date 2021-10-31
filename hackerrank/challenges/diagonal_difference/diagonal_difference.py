# diagonal difference
# https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonal_difference(square_matrix: list[list[int]]) -> int:
    d1 = 0
    d2 = 0

    for i in range(len(square_matrix)):
        d1 += square_matrix[i][i]
        d2 += square_matrix[i][-1 - i]

    return abs(d1 - d2)
