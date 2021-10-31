from bon_appetit import bon_appetit


def test_case_0(capsys):
    bon_appetit([3, 10, 2, 9], 1, 12)
    captured = capsys.readouterr()
    assert '5\n' == captured.out


def test_case_1(capsys):
    bon_appetit([3, 10, 2, 9], 1, 7)
    captured = capsys.readouterr()
    assert "Bon Appetit\n" == captured.out
