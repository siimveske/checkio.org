from datetime import datetime


def date_time(time: str) -> str:
    t = datetime.strptime(time, '%d.%m.%Y %H:%M')

    hour = 'hour' if t.hour == 1 else 'hours'
    minute = 'minute' if t.minute == 1 else 'minutes'

    result = t.strftime(f"{t.day} %B %Y year {t.hour} {hour} {t.minute} {minute}")
    return result


if __name__ == '__main__':

    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    assert date_time("19.09.2999 01:59") == "19 September 2999 year 1 hour 59 minutes"
    assert date_time("21.10.1999 18:01") == "21 October 1999 year 18 hours 1 minute"

    print("OK")
