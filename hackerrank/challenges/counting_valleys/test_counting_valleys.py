from counting_valleys import counting_valleys


def test_case_0():
    assert counting_valleys(8, "UDDDUDUU") == 1


def test_case_1():
    assert counting_valleys(12, "DDUUDDUDUUUD") == 2
