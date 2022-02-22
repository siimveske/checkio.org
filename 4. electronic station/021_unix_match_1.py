import re


def unix_match(filename: str, pattern: str) -> bool:

    re_pattern = pattern.replace('.', r'\.')
    re_pattern = re_pattern.replace('*', '.*')
    re_pattern = re_pattern.replace('?', '.{1}')
    result = re.match(re_pattern, filename)

    return bool(result)


if __name__ == '__main__':
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    assert unix_match("txt", "????*") == False
    assert unix_match("12apache1", "*.*") == False

    print("OK")
