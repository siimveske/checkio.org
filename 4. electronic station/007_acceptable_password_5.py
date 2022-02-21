'''
Create a password verification function.

Those are the verification conditions:
    - the length should be bigger than 6
    - should contain at least one digit, but cannot consist of just digits
    - having numbers or containing just numbers does not apply to the password longer than 9
    - a string should not contain the word "password" in any case
'''


def is_acceptable_password(pwd: str) -> bool:
    length = len(pwd)
    numbers = sum(c.isdigit() for c in pwd)
    letters = sum(c.isalpha() for c in pwd)
    contains_pwd = 'password' in pwd.lower()
    if length > 9:
        return contains_pwd == False
    else:
        return length > 6 and numbers >= 1 and letters > 0 and contains_pwd == False


if __name__ == '__main__':
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    assert is_acceptable_password("password12345") == False
    assert is_acceptable_password("PASSWORD12345") == False
    assert is_acceptable_password("pass1234word") == True

    print("OK")
