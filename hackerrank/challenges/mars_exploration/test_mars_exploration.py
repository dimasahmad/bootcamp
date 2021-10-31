from mars_exploration import mars_exploration


def test_case_0():
    assert mars_exploration("SOSSPSSQSSOR") == 3


def test_case_1():
    assert mars_exploration("SOSSOT") == 1


def test_case_11():
    assert mars_exploration("SOSSOSSOS") == 0