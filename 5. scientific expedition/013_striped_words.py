'''
https://py.checkio.org/en/mission/striped-words/
'''

import string

VOWELS = set("AEIOUY")
SEPARATORS = set(' ') | set(string.punctuation)


def checkio(line: str) -> str:
    line = line.upper()

    words = []
    accumulator = []
    is_word = True

    # Parse words
    for char in line:
        char = char.upper()
        if char in SEPARATORS:
            if accumulator and is_word:
                words.append(''.join(accumulator))
            accumulator.clear()
            is_word = True
        else:
            if char.isdigit():
                is_word = False
            else:
                accumulator.append(char)
    if accumulator and is_word:
        words.append(''.join(accumulator))

    # Count striped words
    cnt = 0
    for word in words:
        if len(word) == 1:
            continue

        striped = True
        for idx in range(len(word) - 1):
            a, b = word[idx], word[idx + 1]
            if a.isdigit() or b.isdigit():
                striped = False
                break
            if (a in VOWELS) != (b in VOWELS):
                continue
            else:
                striped = False
                break

        if striped:
            cnt += 1

    return cnt


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
