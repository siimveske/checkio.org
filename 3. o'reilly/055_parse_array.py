
WHITESPACE_STR = ' \t\n\r'


def parse_array(s: str, _w=WHITESPACE_STR, _sep=","):

    info = {}
    s = s.strip()

    for c in s:
        info.setdefault(c, 0)
        info[c] += 1

    if '[' not in info or ']' not in info:
        raise ValueError
    if info['['] != info[']']:
        raise ValueError
    if ',,' in ''.join([i for i in s if i not in WHITESPACE_STR]):
        raise ValueError
    if not s.startswith('[') or not s.endswith(']'):
        raise ValueError

    result = None
    stack = []
    acc = ''
    last_char = ''

    for c in s:
        if c.isdigit() and last_char == ']':
            raise ValueError
        if c == '[' and last_char.isdigit():
            raise ValueError
        if c == '[' and last_char == ']':
            raise ValueError

        if c == '[':
            stack.append(list())
            acc = ''
        elif c == ']':
            if acc:
                stack[-1].append(int(acc))
                acc = ''
            tmp = stack.pop()
            if not stack:
                if result:
                    raise ValueError
                result = tmp
            else:
                stack[-1].append(tmp)
        elif c == ',':
            if acc:
                stack[-1].append(int(acc))
                acc = ''
        else:
            if c.isalpha():
                raise ValueError
            acc += c
        last_char = c

    return result


if __name__ == "__main__":

    assert parse_array("[1, 2, 3]") == [1, 2, 3], "Simple"
    assert parse_array("[[1], 2, 3]") == [[1], 2, 3], "Nested"
    assert parse_array("[-3, [-2, 0], 10]") == [-3, [-2, 0], 10], "Negative integers"
    assert parse_array("[100]") == [100], "One number"
    assert parse_array("[2,     3]") == [2, 3], "Whitespaces"
    assert parse_array("[[10, [11]], [[[1], 2], 3], 5]") == [[10, [11]], [[[1], 2], 3], 5], "Deep nested"
    assert parse_array("   [3, 4]   ") == [3, 4], "Skip whitespaces"
    assert parse_array("[[], 0]") == [[], 0], "Empty arrays"
    assert parse_array("[[0,], 0]") == [[0], 0], "Comma - closed bracket"

    try:
        parse_array("[asd]")
        assert False, "Only integers"
    except ValueError:
        pass

    try:
        parse_array("[2, 3]]")
        assert False, "Excess bracket"
    except ValueError:
        pass

    try:
        parse_array("[++2, 1]")
        assert False, "Two plus"
    except ValueError:
        pass

    try:
        parse_array("[10, 11, , 12]")
        assert False, "Two separators"
    except ValueError:
        pass

    try:
        parse_array(" 13 ")
        assert False, "Where is a list?"
    except ValueError:
        pass

    try:
        parse_array("[[2]")
        assert False, "Excess opened bracket"
    except ValueError:
        pass

    try:
        parse_array("[3 4]")
        assert False, "Check for spurious spaces within a number"
    except ValueError:
        pass

    try:
        parse_array("[10, 11,, 12]")
        assert False, "Check for double separators without a space in between"
    except ValueError:
        pass

    try:
        parse_array("[[]3]")
        assert False, "Check for missing separators after []"
    except ValueError:
        pass

    try:
        parse_array("[2[]]")
        assert False, " Check for missing separators before []"
    except ValueError:
        pass

    try:
        parse_array("[3],")
        assert False, "Excess separator"
    except ValueError:
        pass

    try:
        parse_array("[1,2]3")
        assert False, "Excess number"
    except ValueError:
        pass

    try:
        parse_array("[1], [2,3]")
        assert False, "Here should be only one array."
    except ValueError:
        pass

    # Extra/0
    assert parse_array("[999, 0, -999, []]") == [999, 0, -999, []]

    # Extra/1
    try:
        parse_array("[[[[1], 2][]]]")
        assert False, "Missing separator"
    except ValueError:
        pass
