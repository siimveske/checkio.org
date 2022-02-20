'''
Create a password verification function.

Those are the verification conditions:
    - the length should be bigger than 6
    - should contain at least one digit, but cannot consist of just digits
    - if the password is longer than 9 - previous rule (about one digit), is not required.
'''


def is_acceptable_password(pwd: str) -> bool:
    length = len(pwd)
    numbers = sum(c.isdigit() for c in pwd)
    letters = sum(c.isalpha() for c in pwd)
    if length > 9:
        return True
    else:
        return length > 6 and numbers >= 1 and letters > 0


if __name__ == '__main__':
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True

    print("OK")
