from library_fine import library_fine


def test_case_1():
    assert library_fine(9, 6, 2015, 6, 6, 2015) == 45


def test_case_5():
    assert library_fine(2, 7, 1014, 1, 1, 1015) == 0


def test_case_10():
    assert library_fine(28, 2, 2015, 15, 4, 2015) == 0