from factorial import factorial


def test_2():
    assert factorial(2) == 2


def test_6():
    assert factorial(6) == 720


def test_3():
    assert factorial(3) == 6


def test_12():
    assert factorial(12) == 479001600


def test_5():
    assert factorial(5) == 120
