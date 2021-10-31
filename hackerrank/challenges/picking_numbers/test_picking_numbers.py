from picking_numbers import picking_numbers


def test_case_0():
    assert picking_numbers([4, 6, 5, 3, 3, 1]) == 3


def test_case_1():
    assert picking_numbers([1, 2, 2, 3, 1, 2]) == 5
