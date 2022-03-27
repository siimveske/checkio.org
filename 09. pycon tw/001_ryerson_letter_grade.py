'''https://py.checkio.org/en/mission/ryerson-letter-grade/'''


def ryerson_letter_grade(pct: int) -> str:
    '''Convert grade percentage to grade letter
    url: https://www.ryerson.ca/studentguide/grades/
    '''
    if pct >= 90:
        return 'A+'
    if 85 <= pct <= 89:
        return 'A'
    if 80 <= pct <= 84:
        return 'A-'
    if 77 <= pct <= 79:
        return 'B+'
    if 73 <= pct <= 76:
        return 'B'
    if 70 <= pct <= 72:
        return 'B-'
    if 67 <= pct <= 69:
        return 'C+'
    if 63 <= pct <= 66:
        return 'C'
    if 60 <= pct <= 62:
        return 'C-'
    if 57 <= pct <= 59:
        return 'D+'
    if 53 <= pct <= 56:
        return 'D'
    if 50 <= pct <= 52:
        return 'D-'

    return 'F'


if __name__ == '__main__':
    assert ryerson_letter_grade(45) == "F"
    assert ryerson_letter_grade(62) == "C-"
    print("OK")
