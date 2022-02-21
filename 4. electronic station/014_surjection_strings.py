def isometric_strings(a, b):
    if len(a) != len(b):
        return False

    memo = {}

    for i in range(len(a)):
        char_a, char_b = a[i], b[i]
        if char_a not in memo:
            memo[char_a] = char_b
        elif memo[char_a] != char_b:
            return False

    return True


if __name__ == "__main__":
    assert isometric_strings("add", "egg") == True
    assert isometric_strings("foo", "bar") == False
    assert isometric_strings("", "") == True
    assert isometric_strings("all", "all") == True
    assert isometric_strings("gogopy", "doodle") == False
    assert isometric_strings("bar", "foo") == True
    print("Coding complete")
