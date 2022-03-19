'''
https://py.checkio.org/en/mission/morse-clock/
'''


def checkio(time_string: str) -> str:
    TO_MORSE = str.maketrans('01', '.-')
    fmt = "{:02b} {:04b} : {:03b} {:04b} : {:03b} {:04b}"
    h, m, s = (divmod(int(n), 10) for n in time_string.split(':'))
    return fmt.format(*h, *m, *s).translate(TO_MORSE)


if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--."
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-."
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-"
    print("OK")
