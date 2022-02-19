
def replace_last(line: list) -> list:
    return line[-1:] + line[:-1]


if __name__ == '__main__':

    assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
    assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert replace_last([1]) == [1]
    assert replace_last([]) == []

    print("OK")
