import re


def unix_match(filename: str, pattern: str) -> bool:

    regex = _escape(pattern)
    regex = regex.replace('.', r'\.')

    regex = regex.replace(r'\\*', r'XXX')
    regex = regex.replace(r'\\?', r'YYY')

    regex = regex.replace('*', '.*')
    regex = regex.replace('?', '.')

    regex = regex.replace(r'XXX', r'\\*')
    regex = regex.replace(r'YYY', r'\\?')

    regex = regex.replace('[]', '')

    result = re.match(regex, filename)

    return bool(result)


def _escape(text):
    charsets = re.search(r'\[(.*)\]', text)
    if charsets:
        for cset in charsets.groups():
            charset = set(cset)
            text = text.replace(cset, re.escape(''.join(charset)))
    return text


if __name__ == '__main__':
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    assert unix_match("[?*]", "[[][?][*][]]") == True
    assert unix_match("name.txt", "name[]txt") == False
    print("OK")
