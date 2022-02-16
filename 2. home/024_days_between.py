'''
You are given two dates as an array with three numbers - a year, month and day. For example: 19 April 1982 will be (1982, 4, 19). You should find the difference in days between the given dates. For example between today and tomorrow = 1 day. The difference will always be either a positive number or zero, so don't forget about the absolute value.
'''

import datetime


def days_diff(a, b):

    d1 = datetime.date(*a)
    d2 = datetime.date(*b)

    diff = d1 - d2

    result = abs(diff.days)
    return result


if __name__ == '__main__':

    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238

    print("OK")
