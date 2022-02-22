import re


def unix_match(filename: str, pattern: str) -> bool:

    if '[]' in pattern:
        return False

    re_pattern = pattern.replace('.', r'\.')
    re_pattern = re_pattern.replace('[!]', 'MUFFIN')
    re_pattern = re_pattern.replace('!', '^')
    re_pattern = re_pattern.replace('MUFFIN', r'\[!\]')
    result = re.match(re_pattern, filename)

    return bool(result)


if __name__ == '__main__':
    assert unix_match("somefile.txt", "somefile.txt") == True
    assert unix_match("1name.txt", "[!abc]name.txt") == True
    assert unix_match("log1.txt", "log[!0].txt") == True
    assert unix_match("log1.txt", "log[1234567890].txt") == True
    assert unix_match("log1.txt", "log[!1].txt") == False
    assert unix_match("name.txt", "name[]txt") == False
    assert unix_match("[!]check.txt", "[!]check.txt") == True
    print("OK")
