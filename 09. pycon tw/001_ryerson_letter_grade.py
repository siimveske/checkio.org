'''https://py.checkio.org/en/mission/ryerson-letter-grade/'''


GRADE_MAP = (
    (90, 'A+'),
    (85, 'A'),
    (80, 'A-'),
    (77, 'B+'),
    (73, 'B'),
    (70, 'B-'),
    (67, 'C+'),
    (63, 'C'),
    (60, 'C-'),
    (57, 'D+'),
    (53, 'D'),
    (50, 'D-')
)


def ryerson_letter_grade(pct: int) -> str:
    '''Convert grade percentage to grade letter
    url: https://www.ryerson.ca/studentguide/grades/
    '''
    for points, letter in GRADE_MAP:
        if pct >= points:
            return letter
    return 'F'


if __name__ == '__main__':
    assert ryerson_letter_grade(45) == "F"
    assert ryerson_letter_grade(62) == "C-"
    print("OK")
