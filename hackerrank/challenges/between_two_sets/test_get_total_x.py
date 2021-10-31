from get_total_x import get_total_x


def test_case_0():
    assert get_total_x([2, 4], [16, 32, 96]) == 3


def test_case_8():
    assert get_total_x([3, 4], [24, 48]) == 2
