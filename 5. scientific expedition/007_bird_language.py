'''
https://py.checkio.org/en/mission/bird-language/
'''

VOWELS = "aeiouy"


def translate(text: str) -> str:
    words = text.split()
    translations = []
    for word in words:
        idx = 0
        translated_word = []
        while idx < len(word):
            letter = word[idx]
            translated_word.append(letter)
            idx += 3 if letter in VOWELS else 2
        translations.append(''.join(translated_word))

    return ' '.join(translations)


if __name__ == "__main__":
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"

    print("OK")
