'''https://py.checkio.org/en/mission/house-password/'''


def checkio(data: str) -> bool:
    length = 0
    has_digits = 0
    has_lowercase = 0
    has_uppercase = 0

    for letter in data:
        if letter.isalpha():
            if letter.islower():
                has_lowercase += 1
            else:
                has_uppercase += 1
        else:
            has_digits += 1
        length += 1

    return bool(length >= 10 and has_digits and has_lowercase and has_uppercase)


if __name__ == '__main__':
    assert checkio('A1213pokl') == False
    assert checkio('bAse730onE4') == True
    assert checkio('asasasasasasasaas') == False
    assert checkio('QWERTYqwerty') == False
    assert checkio('123456123456') == False
    assert checkio('QwErTy911poqqqq') == True

    print("OK")
