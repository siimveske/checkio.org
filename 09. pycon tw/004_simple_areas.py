'''https://py.checkio.org/en/mission/simple-areas/'''
import math


def circle(diameter):
    return (diameter / 2)**2 * math.pi


def rectangle(width, height):
    return width * height


def triangle(a, b, c):
    s = (a + b + c) / 2  # half the perimeter
    return math.sqrt(s * (s - a) * (s - b) * (s - c))  # Heron's Formula


def simple_areas(*args):
    area_function = {1: circle, 2: rectangle, 3: triangle}[len(args)]
    area = area_function(*args)
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
