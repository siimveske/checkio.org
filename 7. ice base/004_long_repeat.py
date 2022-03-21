'''https://py.checkio.org/en/mission/long-repeat/'''


def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    if not line:
        return 0

    cnt = 1
    longest = 0

    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            cnt += 1
        else:
            longest = max(cnt, longest)
            cnt = 1
    longest = max(cnt, longest)

    return longest


if __name__ == '__main__':

    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"

    print('OK')
