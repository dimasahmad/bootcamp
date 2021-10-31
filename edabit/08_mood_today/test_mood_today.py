from mood_today import mood_today

def test_happy():
    assert mood_today("happy") == "Today, I am feeling happy"

def test_sad():
    assert mood_today("sad") == "Today, I am feeling sad"

def test_very_happy():
    assert mood_today("very happy") == "Today, I am feeling very happy"

def test_rather_empty_inside():
    assert mood_today("rather empty inside") == "Today, I am feeling rather empty inside"

def test__confused():
    assert mood_today("confused") == "Today, I am feeling confused"

def test_neutral():
    assert mood_today() == "Today, I am feeling neutral"
