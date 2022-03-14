def checkio(line1: str, line2: str) -> str:
    return ''


if __name__ == '__main__':
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three', 'four,five,one,two,six,three') == 'one,three,two'
    print("OK")
