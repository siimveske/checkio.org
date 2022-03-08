import math


def rounded(f):
    return lambda x: round(f(x), 2)


class Parameters:
    def __init__(self, param):
        self.param = param
        self.figure = None

    def choose_figure(self, figure):
        figure.param = self.param
        self.figure = figure

    @rounded
    def perimeter(self):
        return self.figure.perimeter(self.param)

    @rounded
    def area(self):
        return self.figure.area(self.param)

    @rounded
    def volume(self):
        return self.figure.volume(self.param)


class Figure2D:
    def volume(*_):
        return 0

    def perimeter(self, side_length):
        return self.sides * side_length


class Circle(Figure2D):
    def perimeter(self, radius):
        return 2 * math.pi * radius

    def area(self, radius):
        return math.pi * radius**2


class Triangle(Figure2D):
    sides = 3

    def area(self, side):
        return (math.sqrt(3.0) / 4.0) * side**2


class Square(Figure2D):
    sides = 4

    def area(self, side):
        return side**2


class Pentagon(Figure2D):
    sides = 5

    def area(self, side):
        return (1.0 / 4.0) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side**2


class Hexagon(Figure2D):
    sides = 6

    def area(self, side):
        return ((3 * math.sqrt(3)) / 2) * side**2


class Cube:
    def perimeter(self, side):
        return 12 * side

    def area(self, side):
        return side**2 * 6

    def volume(self, side):
        return side**3


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
