from apple_and_orange import count_apples_and_oranges


def test_case_0(capsys):
    count_apples_and_oranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
    captured = capsys.readouterr()
    assert (
        "1\n"
        "1"
    ) in captured.out
