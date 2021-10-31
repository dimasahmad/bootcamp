from count_ones import count_ones


def test_12():
    assert count_ones(12) == 2


def test_0():
    assert count_ones(0) == 0


def test_100():
    assert count_ones(100) == 3


def test_101():
    assert count_ones(101) == 4


def test_999():
    assert count_ones(999) == 8


def test_123456789():
    assert count_ones(123456789) == 16


def test_1234567890():
    assert count_ones(1234567890) == 12
