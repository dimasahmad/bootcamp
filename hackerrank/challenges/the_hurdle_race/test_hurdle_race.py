from hurdle_race import hurdle_race


def test_case_0():
    assert hurdle_race(4, [1, 6, 3, 5, 2]) == 2


def test_case_1():
    assert hurdle_race(7, [2, 5, 4, 5, 2]) == 0
