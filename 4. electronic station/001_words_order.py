'''
Check if the words in a list appear in the same order as in the given text
    - a word from the list is not in the text - your function should return False;
    - any word can appear more than once in a text - use only the first one;
    - two words in the given list are the same - your function should return False;
    - the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
    - the text includes only English letters and spaces.
'''


def words_order(text: str, words: list) -> bool:
    idx = 0
    visited = set()
    txt = text.split()

    for word in words:
        if word in visited:
            return False

        try:
            result = txt.index(word, idx)
            idx = result + 1
            visited.add(word)
        except ValueError:
            return False

    return True


if __name__ == '__main__':
    assert words_order("hi world im here", ["world", "here"]) == True
    assert words_order("hi world im here", ["here", "world"]) == False
    assert words_order("hi world im here", ["world"]) == True
    assert words_order("hi world im here", ["world", "here", "hi"]) == False
    assert words_order("hi world im here", ["world", "im", "here"]) == True
    assert words_order("hi world im here", ["world", "hi", "here"]) == False
    assert words_order("hi world im here", ["world", "world"]) == False
    assert words_order("hi world im here", ["country", "world"]) == False
    assert words_order("hi world im here", ["wo", "rld"]) == False
    assert words_order("", ["world", "here"]) == False

    print("OK")
