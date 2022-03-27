'''https://py.checkio.org/en/mission/simple-areas/'''
import math


def simple_areas(*args) -> float:
    n = len(args)
    area = 0

    if n == 1:
        r = args[0] / 2  # diameter to radius
        area = math.pi * r**2
    elif n == 2:
        a, b = args  # sides
        area = a * b
    else:
        a, b, c = args  # sides
        s = (a + b + c) / 2  # half the perimeter
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Heron's Formula

    return round(area, 2)


if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"

    print('OK')
