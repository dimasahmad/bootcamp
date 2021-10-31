import datetime
from time_for_milk_and_cookies import time_for_milk_and_cookies


def test_2013_12_24():
    assert time_for_milk_and_cookies(datetime.date(2013, 12, 24)) == True


def test_3000_12_24():
    assert time_for_milk_and_cookies(datetime.date(3000, 12, 24)) == True


def test_2013_1_23():
    assert time_for_milk_and_cookies(datetime.date(2013, 1, 23)) == False


def test_2010_11_2():
    assert time_for_milk_and_cookies(datetime.date(2010, 11, 2)) == False


def test_1980_9_24():
    assert time_for_milk_and_cookies(datetime.date(1980, 9, 24)) == False
