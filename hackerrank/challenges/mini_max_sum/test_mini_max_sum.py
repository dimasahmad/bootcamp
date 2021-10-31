from mini_max_sum import mini_max_sum


def test_case_0(capsys):
    mini_max_sum([1, 2, 3, 4, 5])
    captured = capsys.readouterr()
    assert "10 14" in captured.out


def test_case_14(capsys):
    mini_max_sum([7, 69, 2, 221, 8974])
    captured = capsys.readouterr()
    assert "299 9271" in captured.out
