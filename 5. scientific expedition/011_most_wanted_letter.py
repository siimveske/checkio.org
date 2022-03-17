'''
https://py.checkio.org/en/mission/most-wanted-letter/
'''

import string


def checkio(text: str) -> str:
    '''
    Iterate through latyn alphabet and count each letter in the text.
    'max()' selects the most frequent letter. If multiple items are maximal,
    the max() returns the first one encountered
    '''
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)


if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."

    print("OK")
