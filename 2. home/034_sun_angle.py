from typing import Union
from datetime import datetime


def sun_angle(time: str) -> Union[int, str]:
    t = datetime.strptime(time, '%H:%M')
    if t.hour < 6 or (t.hour >= 18 and t.minute > 0):
        return "I don't see the sun!"

    hour = int(t.strftime("%H"))
    minute = int(t.strftime("%M"))
    delta = (hour - 6) * 3600 + (minute * 60)
    result = (15.0 * delta) / 3600.0

    return round(result, 2)


if __name__ == '__main__':

    assert sun_angle("07:00") == 15
    assert sun_angle("12:15") == 93.75
    assert sun_angle("01:23") == "I don't see the sun!"

    print("OK")
