"""
Find an index of the second occurrence of the second string in the first one
"""


def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    cnt = 0
    for idx, letter in enumerate(text):
        if letter == symbol:
            cnt += 1
        if cnt == 2:
            return idx
    return None


if __name__ == '__main__':

    assert second_index("sims", "s") == 3
    assert second_index("find the river", "e") == 12
    assert second_index("hi", " ") is None
    assert second_index("hi mayor", " ") is None
    assert second_index("hi mr Mayor", " ") == 5

    print("OK")
