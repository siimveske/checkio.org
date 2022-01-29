def max_digit(number: int) -> int:
    """You have a number and you need to determine which digit
    in this number is the biggest."""
    return int(max(str(number)))


if __name__ == '__main__':

    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1

    print("OK")
