def goes_after(word: str, first: str, second: str) -> bool:
    if first == second:
        return False

    try:
        idx1 = word.index(first)
        idx2 = word.index(second)
        return (idx1 + 1) == idx2
    except ValueError:
        return False


if __name__ == "__main__":
    assert goes_after("world", "w", "o") == True
    assert goes_after("world", "w", "r") == False
    assert goes_after("world", "l", "o") == False
    assert goes_after("panorama", "a", "n") == True
    assert goes_after("list", "l", "o") == False
    assert goes_after("", "l", "o") == False
    assert goes_after("list", "l", "l") == False
    assert goes_after("world", "d", "w") == False
    assert goes_after("transport", "r", "t") == False
    print("OK")
