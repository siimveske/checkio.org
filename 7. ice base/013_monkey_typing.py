'''https://py.checkio.org/en/mission/monkey-typing/'''


def count_words(text: str, words: set) -> int:
    result = set()
    text = text.lower().split()
    for token in text:
        for word in words:
            if word in token:
                result.add(word)
    return len(result)


if __name__ == '__main__':
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("OK")
