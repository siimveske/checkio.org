import re


def unix_match(filename: str, pattern: str) -> bool:

    i, j = 0, 0
    result = []

    while j < len(pattern):
        current = pattern[j]
        if current == '*':
            result.append('.*')
        elif current == '?':
            result.append('.')
        elif current == '.':
            result.append(r'\.')
        elif current == '[':
            j += 1
            content = []
            while j < len(pattern):
                head = pattern[j]
                if head == ']':
                    if content:
                        content = ''.join(content)
                        result.append(f'[{content}]')
                        break
                    else:
                        if j < pattern.rindex(']'):
                            content.append(re.escape(head))
                        else:
                            # we have an empty character set [] in pattern
                            return False
                elif head == '!':
                    if pattern[j + 1] == ']':
                        content.append('!')
                    else:
                        content.append('^')
                else:
                    if head == '[':
                        content.append(re.escape(head))
                    else:
                        content.append(head)
                j += 1
            i = j

        else:
            result.append(current)
        i += 1
        j += 1

    regex = ''.join(result)
    regex = regex.replace('[!]', r'\[!\]')

    result = re.match(regex, filename)
    return bool(result)


def _escape(text):
    charsets = re.search(r'\[(.*)\]', text)
    if charsets:
        for charset in charsets.groups():
            text = text.replace(charset, re.escape(charset))
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
    assert unix_match("[check].txt", "[][]check[][].txt") == True
    assert unix_match("1name.txt", "[!abc]name.txt") == True
    assert unix_match("[!]check.txt", "[!]check.txt") == True
    assert unix_match("Feb 2018", "[A-Z][a-z][a-zA-Z] [2-3][0-4][1-1][5-9]")

    print("OK")
