from beautiful_days import beautiful_days


def test_case_0():
    assert beautiful_days(20, 23, 6) == 2


def test_case_1():
    assert beautiful_days(13, 45, 3) == 33
