import string


def check_pangram(text):
    '''
        is the given text is a pangram.
    '''
    return set(string.ascii_lowercase) <= (set(text.lower()))


if __name__ == '__main__':
    assert check_pangram("The quick brown fox jumps over the lazy dog.")
    assert not check_pangram("ABCDEF")
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!")
    print('OK')
