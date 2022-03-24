'''https://py.checkio.org/en/mission/oil-pie/'''
from fractions import Fraction as frac


def divide_pie(groups: tuple) -> tuple:
    result = frac(1)
    num_of_groups = sum(map(abs, groups))
    for group_size in groups:
        if group_size > 0:
            result -= frac(group_size, num_of_groups)
        else:
            part = frac(abs(group_size), num_of_groups)
            result -= result * part

    return result.as_integer_ratio()


if __name__ == '__main__':
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"
    print("OK")
