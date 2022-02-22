'''
Put all of the integer values into one flat list. The order should be as it was in the original list
'''


def flat_list(array):
    result = []
    for i in array:
        if type(i) is list:
            result += flat_list(i)
        else:
            result.append(i)
    return result


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3]
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]
    print('OK')
