'''https://py.checkio.org/en/mission/end-of-other/'''


def checkio(words_set: set) -> bool:

    for word1 in words_set:
        for word2 in words_set:
            # Second parameter of 1 ensures that True
            # will not be returned for the case when word1 == word2
            if word2.endswith(word1, 1):
                return True
    return False


if __name__ == '__main__':

    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"

    print("OK")
