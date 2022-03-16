'''
https://py.checkio.org/en/mission/loading-cargo/
'''


def checkio(data: list):
    '''Karmarkar-Karp algorithm'''
    data.sort()
    while len(data) > 1:
        a = data.pop()
        b = data.pop()
        data.append(abs(a - b))
        data.sort()

    return data[0]


if __name__ == '__main__':
    assert checkio([10, 10]) == 0
    assert checkio([10]) == 10
    assert checkio([5, 8, 13, 27, 14]) == 3
    assert checkio([5, 5, 6, 5]) == 1
    assert checkio([12, 30, 30, 32, 42, 49]) == 9
    assert checkio([1, 1, 1, 3]) == 0

    # Basics/6
    assert checkio([9, 9, 7, 6, 5]) == 0
    print('OK')
