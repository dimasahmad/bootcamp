from minimum_number import minimum_number


def test_case_0():
    assert minimum_number("Ab1") == 3


def test_case_1():
    assert minimum_number("#HackerRank") == 1


def test_case_27():
    assert minimum_number("4700") == 3


def test_case_64():
    assert minimum_number("AUzs-nV") == 1