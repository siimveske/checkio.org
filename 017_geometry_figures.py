import math


class Parameters:
    def __init__(self, param):
        self.param = param
        self.figure = None

    def choose_figure(self, figure):
        figure.param = self.param
        self.figure = figure

    def perimeter(self):
        return self.figure.perimeter(self.param)

    def area(self):
        return self.figure.area(self.param)

    def volume(self):
        return self.figure.volume(self.param)


class Circle:
    def perimeter(self, radius):
        return round(2 * math.pi * radius, 2)

    def area(self, radius):
        return round(math.pi * radius**2, 2)

    def volume(self, *args, **kwargs):
        return 0


class Triangle:
    def perimeter(self, side):
        return round(3 * side, 2)

    def area(self, side):
        result = (math.sqrt(3.0) / 4.0) * side**2
        return round(result, 2)

    def volume(self, *args, **kwargs):
        return 0


class Square:
    def perimeter(self, side):
        return round(4 * side, 2)

    def area(self, side):
        return round(side**2, 2)

    def volume(self, *args, **kwargs):
        return 0


class Pentagon:
    def perimeter(self, side):
        return round(5 * side, 2)

    def area(self, side):
        result = (1.0 / 4.0) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side**2
        return round(result, 2)

    def volume(self, *args, **kwargs):
        return 0


class Hexagon:
    def perimeter(self, side):
        return round(6 * side, 2)

    def area(self, side):
        result = ((3 * math.sqrt(3)) / 2) * side**2
        return round(result, 2)

    def volume(self, *args, **kwargs):
        return 0


class Cube:
    def perimeter(self, side):
        return round(12 * side, 2)

    def area(self, side):
        return round(side**2 * 6, 2)

    def volume(self, side):
        return round(side**3, 2)


if __name__ == '__main__':

    figure = Parameters(10)

    figure.choose_figure(Circle())
    assert figure.area() == 314.16

    figure.choose_figure(Triangle())
    assert figure.perimeter() == 30

    figure.choose_figure(Square())
    assert figure.area() == 100

    figure.choose_figure(Pentagon())
    assert figure.perimeter() == 50

    figure.choose_figure(Hexagon())
    assert figure.perimeter() == 60

    figure.choose_figure(Cube())
    assert figure.volume() == 1000

    print("OK")
