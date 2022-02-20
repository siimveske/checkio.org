"""
https://py.checkio.org/en/mission/reverse-every-ascending/
Create and return a new iterable that contains the same elements as the argument iterable items, but with the reversed order of the elements inside every maximal strictly ascending sublist.
"""


def reverse_ascending(items):

    if len(items) < 2:
        return items

    result = []
    tmp = []

    for i in range(1, len(items)):
        a, b = items[i - 1], items[i]
        if a < b:
            tmp.append(a)
        else:
            tmp.append(a)
            result += sorted(tmp, reverse=True)
            tmp.clear()
        if i == len(items) - 1:
            tmp.append(b)

    result += sorted(tmp, reverse=True)
    return result


if __name__ == '__main__':

    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]

    print("OK")
