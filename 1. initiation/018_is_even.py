def is_even(num: int) -> bool:
    return num % 2 == 0


if __name__ == '__main__':

    assert is_even(2) is True
    assert is_even(5) is False
    assert is_even(0) is True

    print("OK")
