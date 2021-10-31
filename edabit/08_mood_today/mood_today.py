# default mood
# https://edabit.com/challenge/tgEWKRQD8hu5dD3pX


def mood_today(mood: str = "neutral") -> str:
    return f"Today, I am feeling {mood}"


print('mood_today("happy"):\n\t{}'.format(mood_today("happy")))
print('mood_today("sad"):\n\t{}'.format(mood_today("sad")))
print('mood_today("very happy"):\n\t{}'.format(mood_today("very happy")))
print('mood_today("rather empty inside"):\n\t{}'.format(mood_today("rather empty inside")))
print('mood_today("confused"):\n\t{}'.format(mood_today("confused")))
print('mood_today():\n\t{}'.format(mood_today()))