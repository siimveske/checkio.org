'''https://py.checkio.org/en/mission/long-repeat/'''

from itertools import groupby


def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    return max([len(list(g)) for _, g in groupby(line)], default=0)


if __name__ == '__main__':

    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"

    print('OK')
