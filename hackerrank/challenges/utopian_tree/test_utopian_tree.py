from utopian_tree import utopian_tree


def test_case_0():
    assert utopian_tree(0) == 1
    assert utopian_tree(1) == 2


def test_case_1():
    assert utopian_tree(4) == 7
    assert utopian_tree(3) == 6
