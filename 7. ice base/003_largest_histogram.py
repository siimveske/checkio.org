
'''https://py.checkio.org/en/mission/largest-histogram/'''

import random
from helpers import timeit


def largest_histogram(histogram):
    sum = 0
    for i in range(min(histogram), max(histogram) + 1):
        sub_sum = 0
        for n in histogram:
            if n >= i:
                sub_sum += i
            else:
                sub_sum = 0
            if sub_sum > sum:
                sum = sub_sum
    return sum


if __name__ == "__main__":

    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"

    data = [random.randint(50, 500) for _ in range(10000)]
    timeit(largest_histogram, data)
