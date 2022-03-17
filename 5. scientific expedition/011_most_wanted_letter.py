'''
https://py.checkio.org/en/mission/most-wanted-letter/
'''

from collections import defaultdict


def checkio(text: str) -> str:

    stats = defaultdict(int)
    text = text.lower()

    for char in text:
        if char.isalpha():
            stats[char] += 1

    results = sorted(stats.items(), key=lambda x: (-x[1], x[0]))
    return results[0][0]


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
