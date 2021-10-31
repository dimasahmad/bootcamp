from stutters import stutters


def test_increasing():
    assert stutters("increasing") == "in... in... increasing?"


def test_adventures():
    assert stutters("adventures") == "ad... ad... adventures?"


def test_enticing():
    assert stutters("enticing") == "en... en... enticing?"


def test_unacceptable():
    assert stutters("unacceptable") == "un... un... unacceptable?"


def test_accountable():
    assert stutters("accountable") == "ac... ac... accountable?"


def test_incredible():
    assert stutters("incredible") == "in... in... incredible?"


def test_exquisite():
    assert stutters("exquisite") == "ex... ex... exquisite?"

def test_am():
    assert stutters("am") == "am... am... am?"


def test_enduring():
    assert stutters("enduring") == "en... en... enduring?"


def test_outstanding():
    assert stutters("outstanding") == "ou... ou... outstanding?"


def test_astonishing():
    assert stutters("astonishing") == "as... as... astonishing?"


def test_astounding():
    assert stutters("astounding") == "as... as... astounding?"


def test_impressive():
    assert stutters("impressive") == "im... im... impressive?"


def test_revolutionize():
    assert stutters("revolutionize") == "re... re... revolutionize?"


def test_recurring():
    assert stutters("recurring") == "re... re... recurring?"


def test_recollection():
    assert stutters("recollection") == "re... re... recollection?"

def test_so():
    assert stutters("so") == "so... so... so?"


def test_gorgeous():
    assert stutters("gorgeous") == "go... go... gorgeous?"


def test_captivating():
    assert stutters("captivating") == "ca... ca... captivating?"
