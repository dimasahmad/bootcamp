from save_the_prisoner import save_the_prisoner


def test_case_0a():
    assert save_the_prisoner(5, 2, 1) == 2


def test_case_0b():
    assert save_the_prisoner(5, 2, 2) == 3


def test_case_1a():
    assert save_the_prisoner(7, 19, 2) == 6


def test_case_1b():
    assert save_the_prisoner(3, 7, 3) == 3
