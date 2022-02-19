from collections import Counter


def is_majority(items: list) -> bool:
    cnt = Counter(items)
    return cnt[True] > cnt[False]


if __name__ == '__main__':

    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False

    print("OK")
