'''
Create a password verification function.

Those are the verification conditions:
    - the length should be bigger than 6
    - should contain at least one digit
'''


def is_acceptable_password(pwd: str) -> bool:
    length = len(pwd)
    numbers = sum(c.isdigit() for c in pwd)
    return length >= 6 and numbers >= 1


if __name__ == '__main__':
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False

    print("OK")
