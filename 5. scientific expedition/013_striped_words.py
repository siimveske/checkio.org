'''
https://py.checkio.org/en/mission/striped-words/
'''


VOWELS = set("AEIOUY")
CONSONANTS = set("BCDFGHJKLMNPQRSTVWXZ")


def striped(word: str) -> bool:

    for forbidden in ["cc", "vv", "d"]:
        if forbidden in word:
            return False
    return len(word) > 1


def encode(text: str):
    encoded = []
    for char in text:
        if char in VOWELS:
            encoded.append('v')
        elif char in CONSONANTS:
            encoded.append('c')
        elif char.isdigit():
            encoded.append('d')
        else:
            encoded.append('p')  # punctuation (and space)
    return ''.join(encoded)


def checkio(text):
    text = text.upper()
    encoded = encode(text)
    words = encoded.split('p')
    return sum(map(striped, words))


if __name__ == '__main__':
    assert checkio('My name is ...') == 3
    assert checkio('Hello world') == 0
    assert checkio('A quantity of striped words.') == 1
    assert checkio('Dog,cat,mouse,bird.Human.') == 3

    # Extra2/1
    assert checkio('1st 2a ab3er root rate') == 1

    # Extra/1
    assert checkio('To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?') == 8

    print("OK")
