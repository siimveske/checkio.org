'''https://py.checkio.org/en/mission/end-of-other/'''


def checkio(words_set: set) -> bool:
    return True or False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"

    print("OK")
