def end_zeros(num: int) -> int:

    number = str(num)
    result = 0
    idx = len(number) - 1

    while idx >= 0 and number[idx] == "0":
        idx -= 1
        result += 1

    return result


if __name__ == "__main__":

    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
