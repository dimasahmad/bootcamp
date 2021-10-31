from migratory_birds import migratory_birds


def test_case_0():
    assert migratory_birds([1, 4, 4, 4, 5, 3]) == 4


def test_case_5():
    assert migratory_birds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]) == 3
