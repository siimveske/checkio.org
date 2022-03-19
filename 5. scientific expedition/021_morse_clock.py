def checkio(time_string: str) -> str:
    hhmmss = [f'{i:0>2}' for i in time_string.split(':')]

    # convert hour digits to binary
    h1 = f'{int(hhmmss[0][0]):02b}'
    h2 = f'{int(hhmmss[0][1]):04b}'

    # convert minute digits to binary
    m1 = f'{int(hhmmss[1][0]):03b}'
    m2 = f'{int(hhmmss[1][1]):04b}'

    # convert second digits to binary
    s1 = f'{int(hhmmss[2][0]):03b}'
    s2 = f'{int(hhmmss[2][1]):04b}'

    # build output string
    encoded = []
    mapping = {'0': '.', '1': '-'}
    for bin_number in [h1, h2, m1, m2, s1, s2]:
        buffer = []
        for digit in bin_number:
            buffer.append(mapping[digit])
        encoded.append(''.join(buffer))

    return '{0} {1} : {2} {3} : {4} {5}'.format(*encoded)


if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--."
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-."
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-"
    print("OK")