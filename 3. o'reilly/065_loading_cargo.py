'''
https://py.checkio.org/en/mission/loading-cargo/
https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
'''


def checkio(data: list):
    n = len(data)
    result = findMin(data, n)
    return result


def findMinRec(arr, i, sumCalculated,
               sumTotal):

    # If we have reached last element.
    # Sum of one subset is sumCalculated,
    # sum of other subset is sumTotal-
    # sumCalculated.  Return absolute
    # difference of two sums.
    if (i == 0):
        return abs((sumTotal - sumCalculated) -
                   sumCalculated)

    # For every item arr[i], we have two choices
    # (1) We do not include it first set
    # (2) We include it in first set
    # We return minimum of two choices
    return min(findMinRec(arr, i - 1,
                          sumCalculated + arr[i - 1],
                          sumTotal),
               findMinRec(arr, i - 1,
                          sumCalculated, sumTotal))

# Returns minimum possible
# difference between sums
# of two subsets


def findMin(arr, n):

    # Compute total sum
    # of elements
    sumTotal = 0
    for i in range(n):
        sumTotal += arr[i]

    # Compute result using
    # recursive function
    return findMinRec(arr, n, 0, sumTotal)


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
