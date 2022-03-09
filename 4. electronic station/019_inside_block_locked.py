'''
https://py.checkio.org/en/mission/inside-block/
https://stackoverflow.com/questions/36399381/whats-the-fastest-way-of-checking-if-a-point-is-inside-a-polygon-in-python
'''
from typing import Tuple


def is_inside(polygon: Tuple[Tuple[int, int], ...], point: Tuple[int, int]) -> bool:

    if point in polygon:
        return True

    x, y = point

    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]

        # Test if Point is on a vertical (y) line
        if x == p1x and x == p2x:
            if (min(p1y, p2y) <= y <= max(p1y, p2y)):
                return True

        # Test if Point is on a horizontal (x) line
        if y == p1y and y == p2y:
            if (min(p1x, p2x) <= x <= max(p1x, p2x)):
                return True

        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside


if __name__ == '__main__':
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)), (2, 2)) is True
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)), (4, 2)) is False
    assert is_inside(((1, 1), (4, 1), (2, 3)), (3, 2)) is True
    assert is_inside(((1, 1), (4, 1), (1, 3)), (3, 3)) is False
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)), (4, 3)) is True
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)), (4, 3)) is False
    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)), (3, 3)) is True
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)), (4, 3)) is False

    # Extra/0
    assert is_inside([[3, 4], [4, 2], [2, 1], [1, 3]], [2, 2]) == True

    # Extra/3
    assert is_inside([[1, 1], [1, 3], [3, 3], [3, 1]], [1, 1]) == True

    # Extra/13
    assert is_inside([[0, 0], [0, 2], [2, 2], [2, 0]], [1, 0]) == True

    print("OK")
