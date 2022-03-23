'''https://py.checkio.org/en/mission/counting-tiles/'''


def checkio(radius):
    """count tiles"""
    return [0, 0]


if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"

    print('OK')
