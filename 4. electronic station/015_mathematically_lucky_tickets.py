from itertools import product


def possible_results(data):
    yield int(data)
    for i in range(1, len(data)):
        for (x, y) in product(possible_results(data[:i]), possible_results(data[i:])):
            yield from (x + y, x - y, x * y)
            if y:
                yield x / y


def checkio(data):
    return True if 100 not in possible_results(data) else False


if __name__ == '__main__':
    assert checkio('000000') == True, "All zeros"
    assert checkio('707409') == True, "You can not transform it to 100"
    assert checkio('595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"

    print("OK")
