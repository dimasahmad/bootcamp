from sock_merchant import sock_merchant


def test_case_0():
    assert sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]) == 3


def test_case_1():
    assert sock_merchant([1, 1, 3, 1, 2, 1, 3, 3, 3, 3]) == 4
