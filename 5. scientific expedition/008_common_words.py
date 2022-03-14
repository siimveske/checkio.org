'''
https://py.checkio.org/en/mission/common-words/
'''


def checkio(line1: str, line2: str) -> str:
    A = set(line1.split(','))
    B = set(line2.split(','))
    intersection = A.intersection(B)
    return ','.join(sorted(intersection))


if __name__ == '__main__':
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three', 'four,five,one,two,six,three') == 'one,three,two'
    print("OK")
