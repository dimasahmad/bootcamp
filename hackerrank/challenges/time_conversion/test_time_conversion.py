from time_conversion import time_conversion


def test_07_05_45_pm():
    assert time_conversion("07:05:45PM") == "19:05:45"


def test_12_05_45_pm():
    assert time_conversion("12:05:45PM") == "12:05:45"


def test_12_05_45_am():
    assert time_conversion("12:05:45AM") == "00:05:45"
