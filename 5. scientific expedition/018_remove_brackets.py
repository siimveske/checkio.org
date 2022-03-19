'''
https://py.checkio.org/en/mission/remove-brackets/
'''


def is_balanced(data):
    stack = [""]
    brackets = {"(": ")", "[": "]", "{": "}"}
    for c in data:
        if c in brackets:
            stack.append(brackets[c])
        elif c in brackets.values() and c != stack.pop():
            return False
    return stack == [""]


def _remove_brackets(line: str, memo: dict) -> str:
    if not line:
        return ""

    if line in memo:
        return memo[line]

    if is_balanced(line):
        return line

    longest_balanced_line = ""
    for idx in range(len(line)):
        slice = line[:idx] + line[idx + 1:]
        balanced_line = _remove_brackets(slice, memo)
        if len(balanced_line) > len(longest_balanced_line):
            longest_balanced_line = balanced_line

    memo[line] = longest_balanced_line
    return memo[line]


def remove_brackets(line: str) -> str:
    return _remove_brackets(line, {})


if __name__ == "__main__":
    assert remove_brackets("(()()") == "()()"
    assert remove_brackets("[][[[") == "[]"
    assert remove_brackets("[[(}]]") == "[[]]"
    assert remove_brackets("[[{}()]]") == "[[{}()]]"
    assert remove_brackets("[[[[[[") == ""
    assert remove_brackets("[[[[}") == ""
    assert remove_brackets("") == ""
    assert remove_brackets("[(])") == "()"
    print("OK")
