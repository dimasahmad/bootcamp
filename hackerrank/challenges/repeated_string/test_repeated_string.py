from repeated_string import repeated_string


def test_case_0():
    assert repeated_string("aba", 10) == 7


def test_case_1():
    assert repeated_string("a", 1000000000000) == 1000000000000


def test_case_9():
    assert repeated_string(
        "epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq",
        549382313570) == 16481469408
