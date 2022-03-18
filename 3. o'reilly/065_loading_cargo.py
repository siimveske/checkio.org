'''
https://py.checkio.org/en/mission/loading-cargo/
https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
'''


def checkio(data: list):
    '''Return minimum possible difference between sums of two subsets'''

    n = len(data)
    sumTotal = sum(data)
    result = findMinRec(data, n, 0, sumTotal)
    return result


def findMinRec(data, i, sumCalculated, sumTotal):

    # If we have reached last element.
    # Sum of one subset is sumCalculated,
    # sum of other subset is sumTotal-
    # sumCalculated.  Return absolute
    # difference of two sums.
    if (i == 0):
        return abs((sumTotal - sumCalculated) - sumCalculated)

    # For every item arr[i], we have two choices
    # (1) We do not include it first set
    # (2) We include it in first set
    # We return minimum of two choices
    L = findMinRec(data, i - 1, sumCalculated + data[i - 1], sumTotal)
    R = findMinRec(data, i - 1, sumCalculated, sumTotal)
    return min(L, R)


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
