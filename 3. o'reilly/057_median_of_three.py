import statistics
from typing import Iterable
'''
Given an iterable of ints , create and return a new iterable whose first two elements are the same as in items, after which each element equals the median of the three elements in the original list ending in that position.
'''


def median_three(els: Iterable[int]) -> Iterable[int]:
    result = els[0:2]
    for i in range(2, len(els)):
        median = statistics.median(els[i - 2:i + 1])
        result.append(median)
    return result


if __name__ == '__main__':
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([1])) == [1]
    print("OK")
