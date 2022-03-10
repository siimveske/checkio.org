'''
https://py.checkio.org/en/mission/how-deep/
'''


def how_deep(structure):
    if type(structure) is tuple:
        return 1 + max(map(how_deep, structure), default=0)
    return 0


if __name__ == '__main__':
    assert how_deep((1, 2, 3)) == 1
    assert how_deep((1, 2, (3,))) == 2
    assert how_deep((1, 2, (3, (4,)))) == 3
    assert how_deep(()) == 1
    assert how_deep(((),)) == 2
    assert how_deep((((),),)) == 3
    assert how_deep((1, (2,), (3,))) == 2
    assert how_deep((1, ((),), (3,))) == 3
    print("OK")
