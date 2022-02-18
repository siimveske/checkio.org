"""
Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.
"""


def frequency_sort(items: list):

    result = sorted(items, key=lambda x: (-items.count(x), items.index(x)))
    return result


if __name__ == '__main__':

    assert frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert frequency_sort([17, 99, 42]) == [17, 99, 42]
    assert frequency_sort([]) == []
    assert frequency_sort([1]) == [1]

    print("OK")
