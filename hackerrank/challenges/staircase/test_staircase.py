from staircase import staircase


def test_6(capsys):
    staircase(6)
    captured = capsys.readouterr()
    assert ('     #\n'
            '    ##\n'
            '   ###\n'
            '  ####\n'
            ' #####\n'
            '######') in captured.out


def test_3(capsys):
    staircase(3)
    captured = capsys.readouterr()
    assert ('  #\n'
            ' ##\n'
            '###') in captured.out


def test_1(capsys):
    staircase(1)
    captured = capsys.readouterr()
    assert ('#') in captured.out
