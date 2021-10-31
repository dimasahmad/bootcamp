from page_count import page_count


def test_case_0():
    assert page_count(6, 2) == 1


def test_case_1():
    assert page_count(5, 4) == 0
