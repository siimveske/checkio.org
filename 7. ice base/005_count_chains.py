'''https://py.checkio.org/en/mission/count-chains/'''

import itertools
import math
from typing import List, Tuple


def distance(a: Tuple[int, int], b: Tuple[int, int]):
    x1, y1 = a
    x2, y2 = b
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def intersect(a: Tuple[int, int, int], b: Tuple[int, int, int]):
    x1, y1, r1 = a
    x2, y2, r2 = b
    dist = distance((x1, y1), (x2, y2))
    return abs(r2 - r1) < dist < (r1 + r2)


def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    connected = {c: [] for c in circles}
    for i in range(len(circles) - 1):
        for j in range(i + 1, len(circles)):
            a = circles[i]
            b = circles[j]
            if intersect(a, b):
                connected[a].append(b)

    vals = set(itertools.chain(*connected.values()))
    keys = set(connected.keys())
    return len(keys - vals)


if __name__ == '__main__':
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    print("OK")
