'''
https://py.checkio.org/en/mission/boolean-algebra/
'''


def boolean(x, y, operation):
    if operation == "conjunction":
        return int(x and y)
    if operation == "disjunction":
        return int(x or y)
    if operation == "implication":
        return int(not x or y)
    if operation == "exclusive":
        return int((x or y) and not (x and y))
    if operation == "equivalence":
        return int(x == y)


if __name__ == '__main__':

    assert boolean(1, 0, "conjunction") == 0
    assert boolean(1, 0, "disjunction") == 1
    assert boolean(1, 1, "implication") == 1
    assert boolean(0, 1, "exclusive") == 1
    assert boolean(0, 1, "equivalence") == 0

    print('OK')
