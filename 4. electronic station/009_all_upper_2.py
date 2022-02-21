'''
Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return False.
'''


def is_all_upper(text: str) -> bool:
    char_cnt = 0
    for char in text:
        if char.isalpha():
            if char.islower():
                return False
            char_cnt += 1

    return char_cnt > 0


if __name__ == '__main__':
    assert is_all_upper("ALL UPPER") == True
    assert is_all_upper("all lower") == False
    assert is_all_upper("mixed UPPER and lower") == False
    assert is_all_upper("") == False

    print("OK")
