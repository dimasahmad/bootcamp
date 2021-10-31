from breaking_records import breaking_records


def test_case_0():
    assert breaking_records([10, 5, 20, 20, 4, 5, 2, 25, 1]) == [2, 4]


def test_case_1():
    assert breaking_records([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]) == [4, 0]
