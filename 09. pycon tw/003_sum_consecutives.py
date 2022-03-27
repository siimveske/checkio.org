'''https://py.checkio.org/en/mission/sum-consecutives/'''


def sum_consecutives(integers: list) -> list:
    result = []
    stack = []
    for i in integers:
        if stack and stack[-1] != i:
            result.append(sum(stack))
            stack.clear()
        stack.append(i)

    if stack:
        result.append(sum(stack))

    return result


if __name__ == '__main__':
    assert list(sum_consecutives([1, 1, 1, 1])) == [4]
    assert list(sum_consecutives([1, 1, 2, 2])) == [2, 4]
    assert list(sum_consecutives([1, 1, 2, 1])) == [2, 2, 1]
    assert list(sum_consecutives([3, 3, 3, 4, 4, 5, 6, 6])) == [9, 8, 5, 12]
    assert list(sum_consecutives([1])) == [1]
    assert list(sum_consecutives([])) == []

    print("OK")
