'''
https://py.checkio.org/en/mission/mathematically-lucky-tickets/
'''


def divide(data):
    yield int(data)

    # divide 123456: 1 23456, 12 3456, 123 456, ...
    for pos in range(1, len(data)):
        for left in divide(data[:pos]):
            for right in divide(data[pos:]):
                # calculate + - * /
                yield left + right
                yield left - right
                yield left * right
                if right:
                    yield left / right


def checkio(data):
    for x in divide(data):
        if x == 100:
            return False
    return True


if __name__ == '__main__':
    assert checkio('000000') == True, "All zeros"
    assert checkio('707409') == True, "You can not transform it to 100"
    assert checkio('595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"

    print("OK")
