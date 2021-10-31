from plus_minus import plus_minus


def test_case_0(capsys):
    plus_minus([-4, 3, -9, 0, 4, 1])
    captured = capsys.readouterr()
    assert "0.500000\n0.333333\n0.166667" in captured.out


def test_case_1(capsys):
    plus_minus([1, 2, 3, -1, -2, -3, 0, 0])
    captured = capsys.readouterr()
    assert "0.375000\n0.375000\n0.250000" in captured.out
