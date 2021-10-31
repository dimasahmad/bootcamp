from base_2 import dec2bin


def test_100():
    assert dec2bin(100) == "1100100"


def test_1():
    assert dec2bin(1) == "1"


def test_0():
    assert dec2bin(0) == "0"


def test_69():
    assert dec2bin(69) == "1000101"


def test_1023():
    assert dec2bin(1023) == "1111111111"


def test_511():
    assert dec2bin(511) == "111111111"


def test_666():
    assert dec2bin(666) == "1010011010"


def test_123():
    assert dec2bin(123) == "1111011"
