from compare_triplets import compare_triplets


def test_case_0():
    assert compare_triplets([5, 6, 7], [3, 6, 10]) == [1, 1]


def test_case_1():
    assert compare_triplets([17, 28, 30], [99, 16, 8]) == [2, 1]
