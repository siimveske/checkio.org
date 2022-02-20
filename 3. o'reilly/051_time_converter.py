"""
https://py.checkio.org/en/mission/time-converter-12h-to-24h/
"""

from time import strptime
from time import strftime


def time_converter(time: str) -> str:
    raw_time = time.replace('.', '').upper()
    parsed_time = strptime(raw_time, r'%I:%M %p')
    formatted_time = strftime('%H:%M', parsed_time)
    return formatted_time


if __name__ == '__main__':

    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'

    print("OK")
