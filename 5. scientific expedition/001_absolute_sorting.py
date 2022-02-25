def checkio(values: list) -> list:
    values.sort(key=lambda x: abs(x))
    return values


if __name__ == '__main__':
    assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
    assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
    assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
    print("OK")
