'''
https://py.checkio.org/en/mission/bird-language/
'''

VOWELS = "aeiouy"


def translate(text: str) -> str:

    idx = 0
    translation = []

    while idx < len(text):
        letter = text[idx]
        translation.append(letter)
        if letter == ' ':
            idx += 1
        elif letter in VOWELS:
            idx += 3
        else:
            idx += 2

    return ''.join(translation)


if __name__ == "__main__":
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"

    print("OK")
