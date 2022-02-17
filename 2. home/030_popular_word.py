"""
Determine the popularity of certain words in the text:
    - The words should be sought in all registers. This means that if you need to find a word "one" then words like "one", "One", "oNe", "ONE" etc. will do.
    - The search words are always indicated in the lowercase.
    - If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value.
"""


def popular_words(text: str, words: list) -> dict:
    result = {}
    for word in words:
        result[word] = 0

    for word in text.split():
        current = word.lower()
        if current in words:
            result[current] += 1

    return result


if __name__ == '__main__':

    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }

    print("OK")
