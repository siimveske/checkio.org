def is_all_upper(text: str) -> bool:

    for letter in text:
        if letter.islower():
            return False

    return True


if __name__ == '__main__':

    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('     ') == True
    assert is_all_upper('444') == True
    assert is_all_upper('55 55 5') == True
    print("OK")
