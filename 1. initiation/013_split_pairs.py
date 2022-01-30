def split_pairs(a):
    if len(a) % 2 != 0:
        a = a+'_'

    result = []
    for i in range(0, len(a), 2):
        result.append(a[i:i+2])

    return result


if __name__ == '__main__':

    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []

    print("OK")
