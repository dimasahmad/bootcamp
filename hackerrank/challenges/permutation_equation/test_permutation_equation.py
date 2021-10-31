from permutation_equation import permutation_equation


def test_case_0():
    assert permutation_equation([2, 3, 1]) == [2, 3, 1]


def test_case_11():
    assert permutation_equation([4, 3, 5, 1, 2]) == [1, 3, 5, 4, 2]
