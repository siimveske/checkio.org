def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))

if __name__ == '__main__':

    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4

    print("OK")
