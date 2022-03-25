'''https://py.checkio.org/en/mission/roman-numerals/'''


LOOKUP = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
]


def checkio(num: int) -> str:
    res = []
    for n, roman in LOOKUP:
        d, num = divmod(num, n)
        res.append(roman * d)
    return ''.join(res)


if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('OK')
