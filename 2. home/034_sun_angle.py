from typing import Union


def sun_angle(time: str) -> Union[int, str]:

    hour, minute = map(int, time.split(':'))

    # 1h == 15deg 1min == 0.25 deg
    angle = ((15 * hour) + (0.25 * minute)) - 90

    return angle if 0 <= angle <= 180 else "I don't see the sun!"


if __name__ == '__main__':

    assert sun_angle("07:00") == 15
    assert sun_angle("12:15") == 93.75
    assert sun_angle("01:23") == "I don't see the sun!"

    print("OK")
