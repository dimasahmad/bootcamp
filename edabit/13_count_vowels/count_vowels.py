# count vowels
# https://edabit.com/challenge/p88k8yHRPTMPt4bBo


def count_vowels(text: str) -> int:
    # convert text to lowercase
    text = text.lower()

    # store counter for each vowels in a dictionary
    vowels_counts = {}

    # iterate vowels
    for vowel in "aeiou":
        # count vowel
        vowel_count = text.count(vowel)
        # store vowel count
        vowels_counts[vowel] = vowel_count

    # sum vowels counters
    vowels_sum = sum(vowels_counts.values())

    return vowels_sum


print('count_vowels("Celebration"):\n\t{}'.format(count_vowels("Celebration")))
print('count_vowels("Palm"):\n\t{}'.format(count_vowels("Palm")))
print('count_vowels("Prediction"):\n\t{}'.format(count_vowels("Prediction")))
print('count_vowels("Suite"):\n\t{}'.format(count_vowels("Suite")))
print('count_vowels("Quote"):\n\t{}'.format(count_vowels("Quote")))
print('count_vowels("Portrait"):\n\t{}'.format(count_vowels("Portrait")))
print('count_vowels("Steam"):\n\t{}'.format(count_vowels("Steam")))
print('count_vowels("Tape"):\n\t{}'.format(count_vowels("Tape")))
print('count_vowels("Nightmare"):\n\t{}'.format(count_vowels("Nightmare")))
print('count_vowels("Convention"):\n\t{}'.format(count_vowels("Convention")))
