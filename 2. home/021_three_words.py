def checkio(words: str) -> bool:
    word_list = words.split()
    if len(word_list) < 3:
        return False

    ctr = 0
    for word in word_list:
        if word.isnumeric():
            ctr = 0
        else:
            ctr += 1
        if ctr == 3:
            break

    return ctr == 3


if __name__ == '__main__':

    assert checkio("Hello World hello") == True
    assert checkio("He is 123 man") == False
    assert checkio("1 2 3 4") == False
    assert checkio("bla bla bla bla") == True
    assert checkio("Hi") == False
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12") == True

    print("OK")
