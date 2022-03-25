'''https://py.checkio.org/en/mission/reverse-roman-numerals/'''


def reverse_roman(roman_string):
    return 0


if __name__ == '__main__':

    assert reverse_roman('VI') == 6
    assert reverse_roman('LXXVI') == 76
    assert reverse_roman('CDXCIX') == 499
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888

    print('OK')
