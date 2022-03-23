'''https://py.checkio.org/en/mission/clock-angle/'''


def clock_angle(time):
    hours, minutes = map(int, time.split(':'))

    hours = hours % 12
    rot_per_hour = 360 / 12
    rot_per_minute = rot_per_hour / 60
    hour_hand = rot_per_hour * hours + rot_per_minute * minutes

    minute_hand = 360 / 60 * minutes
    return 180 - abs(180 - abs(hour_hand - minute_hand))


if __name__ == '__main__':
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"
    print("OK")
