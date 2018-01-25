import random


CONSONANTS = ['f', 'j', 'c', 'l', 'n']
PASSPHRASE = '{}u{}am para as {}o{}i{}as'


def totally_random():
    """Run a totally random way."""
    random.shuffle(CONSONANTS)
    return PASSPHRASE.format(*CONSONANTS)


def switch_two():
    """Run by changing two steps at a time."""
    first = random.randint(0, 1)
    second = random.randint(2, 4)

    CONSONANTS[first], CONSONANTS[second] = CONSONANTS[second], CONSONANTS[first]
    return PASSPHRASE.format(*CONSONANTS)
