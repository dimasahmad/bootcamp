from get_money_spent import get_money_spent


def test_case_0():
    assert get_money_spent([3, 1], [5, 2, 8], 10) == 9


def test_case_1():
    assert get_money_spent([4], [5], 5) == -1
