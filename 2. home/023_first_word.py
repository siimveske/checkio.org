'''
You are given a string where you have to find its first word.

When solving a task pay attention to the following points:
    - There can be dots and commas in a string.
    - A string can start with a letter or, for example, one/multiple dot(s) or space(s).
    - A word can contain an apostrophe and it's a part of a word.
    - The whole text can be represented with one word and that's it.
'''


def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """

    start_idx = 0
    while not text[start_idx].isalpha():
        start_idx += 1

    end_idx = start_idx
    while end_idx < len(text) and (text[end_idx].isalpha() or text[end_idx] == '\''):
        end_idx += 1

    return text[start_idx:end_idx]


if __name__ == '__main__':

    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"

    print("OK")
