def time_converter(time):
    h, m = [int(i) for i in time.split(':')]
    suffix = 'a.m.' if h < 12 else 'p.m.'
    h = (h - 1) % 12 + 1
    return f"{h}:{m:02} {suffix}"


if __name__ == '__main__':
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("OK")
