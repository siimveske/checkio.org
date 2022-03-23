'''https://py.checkio.org/en/mission/counting-tiles/'''

import math


def checkio(radius: float) -> list[int, int]:
    """count tiles"""
    full = 0
    partial = 0
    limit = math.ceil(radius)

    for i in range(limit):
        for j in range(limit):
            top_right = math.hypot(i + 1, j + 1)
            if top_right <= radius:
                full += 1
                continue
            if i == 0 and j == 0:
                partial += 1
                continue
            if math.hypot(i, j) <= radius:
                partial += 1

    return [full * 4, partial * 4]


if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"

    print('OK')
