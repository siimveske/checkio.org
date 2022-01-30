def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    if not array:
        return 0

    result = 0
    total = 0
    for i in range(0, len(array), 2):
        total += array[i]
    result = total * array[-1]

    return result


if __name__ == '__main__':

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"

    print("OK")
