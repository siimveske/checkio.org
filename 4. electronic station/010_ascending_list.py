'''
Determine whether the sequence of elements items is ascending such that each of its elements is strictly larger than (and not merely equal to) the preceding element
'''


from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    for i in range(1, len(items)):
        if items[i - 1] >= items[i]:
            return False
    return True


if __name__ == '__main__':
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False

    print("OK")
