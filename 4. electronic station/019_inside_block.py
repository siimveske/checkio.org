'''
https://py.checkio.org/en/mission/inside-block/
https://stackoverflow.com/questions/36399381/whats-the-fastest-way-of-checking-if-a-point-is-inside-a-polygon-in-python
'''
from typing import Tuple


def is_inside(polygon: Tuple[Tuple[int, int], ...], point: Tuple[int, int]) -> bool:
    x, y = point
    n = len(polygon)
    inside = False

    x1, y1 = polygon[0]
    for i in range(n + 1):
        x2, y2 = polygon[i % n]

        # Test if Point is on a vertical (y) line
        if x == x1 == x2:
            if (min(y1, y2) <= y <= max(y1, y2)):
                return True

        # Test if Point is on a horizontal (x) line
        if y == y1 == y2:
            if (min(x1, x2) <= x <= max(x1, x2)):
                return True

        if y > min(y1, y2):
            if y <= max(y1, y2):
                if x <= max(x1, x2):
                    if y1 != y2:
                        xints = (y - y1) * (x2 - x1) / (y2 - y1) + x1
                    if x1 == x2 or x <= xints:
                        inside = not inside
        x1, y1 = x2, y2

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
