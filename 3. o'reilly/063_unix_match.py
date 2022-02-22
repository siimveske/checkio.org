import re


def unix_match(filename: str, pattern: str) -> bool:
    list = [('.', r'\.'), ('?', '.'), ('[.]', '.'), ('[[]', r'\['), ('[]]', r'\]')]
    x = pattern
    for a, b in list:
        x = x.replace(a, b)
    if '[!]' not in pattern:
        x = x.replace('[!', '[^')
    else:
        x = x.replace('[!]', '\[!\]')
    if '[*]' not in pattern:
        x = x.replace('*', '.+')

    try:
        return bool(re.match(x, filename))
    except:
        return pattern == filename


if __name__ == '__main__':
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    assert unix_match("[?*]", "[[][?][*][]]") == True
    print("OK")
