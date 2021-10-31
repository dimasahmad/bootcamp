from count_vowels import count_vowels


def test_celebration():
    assert count_vowels("Celebration") == 5


def test_palm():
    assert count_vowels("Palm") == 1


def test_prediction():
    assert count_vowels("Prediction") == 4


def test_suite():
    assert count_vowels("Suite") == 3


def test_quote():
    assert count_vowels("Quote") == 3


def test_portrait():
    assert count_vowels("Portrait") == 3


def test_steam():
    assert count_vowels("Steam") == 2


def test_tape():
    assert count_vowels("Tape") == 2


def test_nightmare():
    assert count_vowels("Nightmare") == 3


def test_convention():
    assert count_vowels("Convention") == 4
