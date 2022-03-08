'''https://py.checkio.org/en/mission/brackets/'''


def checkio(expression):
    stack = [""]  # Use empty string as sentinel for pop() IndexError
    brackets = {"(": ")", "[": "]", "{": "}"}
    for c in expression:
        if c in brackets:
            stack.append(brackets[c])
        elif c in brackets.values() and c != stack.pop():
            return False
    return stack == [""]


if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"

    print("OK")
