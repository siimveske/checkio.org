'''
https://py.checkio.org/en/mission/boolean-algebra/
'''

OPERATION_NAMES = {
    "conjunction": lambda x, y: int(x and y),
    "disjunction": lambda x, y: int(x or y),
    "implication": lambda x, y: int(y or not x),
    "exclusive": lambda x, y: int((x or y) and not (x and y)),
    "equivalence": lambda x, y: int(x == y)
}


def boolean(x, y, operation):
    return OPERATION_NAMES.get(operation)(x, y)


if __name__ == '__main__':

    assert boolean(1, 0, "conjunction") == 0
    assert boolean(1, 0, "disjunction") == 1
    assert boolean(1, 1, "implication") == 1
    assert boolean(0, 1, "exclusive") == 1
    assert boolean(0, 1, "equivalence") == 0

    print('OK')
