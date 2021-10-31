from weight import weight


def test_4_10():
    assert weight(4, 10) == 0.5


def test_30_60():
    assert weight(30, 60) == 169.65


def test_15_10():
    assert weight(15, 10) == 7.07


def test_20_40():
    assert weight(20, 40) == 50.27


def test_100_30():
    assert weight(100, 30) == 942.48


def test_200_300():
    assert weight(200, 300) == 37699.11


def test_15_23():
    assert weight(15, 23) == 16.26


def test_22_44():
    assert weight(22, 44) == 66.9
