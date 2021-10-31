from cat_and_mouse import cat_and_mouse


def test_case_0():
    assert cat_and_mouse(1, 2, 3) == "Cat B"
    assert cat_and_mouse(1, 3, 2) == "Mouse C"
