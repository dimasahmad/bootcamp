from birthday import birthday


def test_case_0():
    assert birthday([1, 2, 1, 3, 2], 3, 2) == 2


def test_case_1():
    assert birthday([1, 1, 1, 1, 1, 1], 3, 2) == 0


def test_case_2():
    assert birthday([4], 4, 1) == 1


def test_case_3():
    assert birthday([2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2,
                    1, 4, 1, 3, 3, 4, 2, 1], 18, 7) == 3
