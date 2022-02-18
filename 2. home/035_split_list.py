'''
You have to split a given array into two arrays. If it has an odd amount of elements, then the first array should have more elements. If it has no elements, then two empty arrays should be returned.
'''


def split_list(items: list) -> list:
    if not items:
        return [[], []]

    if len(items) % 2 == 0:
        middle = len(items) // 2
    else:
        middle = (len(items) // 2) + 1

    return [items[:middle], items[middle:]]


if __name__ == '__main__':

    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]

    print("OK")
