from jumping_on_clouds import jumping_on_clouds


def test_case_0():
    assert jumping_on_clouds([0, 0, 1, 0, 0, 1, 1, 0], 2) == 92


def test_case_1():
    assert jumping_on_clouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 3) == 80
