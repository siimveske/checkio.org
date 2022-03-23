'''https://py.checkio.org/en/mission/clock-angle/'''

from datetime import datetime


def clock_angle(time):
    t = datetime.strptime(time, "%H:%M")
    timevalue_12hour = t.strftime("%I:%M")
    hh, mm = [int(i) for i in timevalue_12hour.split(':')]
    m = mm / 60.0
    h = (hh + m) / 12.0

    hdeg = 360 * h
    mdeg = 360 * m
    delta = round(abs(hdeg - mdeg), 2)
    if delta > 180:
        delta = 360 - delta
    return delta


if __name__ == '__main__':
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"
    print("OK")
