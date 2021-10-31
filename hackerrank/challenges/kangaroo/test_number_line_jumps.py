from number_line_jumps import kangaroo

def test_case_0(benchmark):
    assert benchmark(kangaroo, 0, 3, 4, 2) == "YES"

def test_case_1(benchmark):
    assert benchmark(kangaroo, 0, 2, 5, 3) == "NO"

def test_case_23(benchmark):
    assert benchmark(kangaroo, 1817, 9931, 8417, 190) == "NO"

def test_case_24(benchmark):
    assert benchmark(kangaroo, 3585, 7317, 6994, 9610) == "NO"

def test_case_25(benchmark):
    assert benchmark(kangaroo, 1113, 612, 1331, 610) == "YES"

def test_case_26(benchmark):
    assert benchmark(kangaroo, 2081, 8403, 9107, 8400) == "YES"

def test_case_27(benchmark):
    assert benchmark(kangaroo, 1928, 4306, 5763, 4301) == "YES"

def test_case_28(benchmark):
    assert benchmark(kangaroo, 7271, 2211, 7915, 2050) == "YES"

def test_case_29(benchmark):
    assert benchmark(kangaroo, 1571, 4240, 9023, 4234) == "YES"
    