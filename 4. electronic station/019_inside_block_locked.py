'''
https://py.checkio.org/en/mission/inside-block/
'''
from typing import Tuple
from shapely.geometry import Point
from shapely.geometry import Polygon


def is_inside(polygon: Tuple[Tuple[int, int], ...], point: Tuple[int, int]) -> bool:
    point = Point(point)
    polygon = Polygon(polygon)
    return polygon.contains(point) or polygon.touches(point)


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

    print("OK")
