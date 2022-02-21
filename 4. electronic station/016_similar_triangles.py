from math import sqrt
from typing import List, Tuple
Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:

    sides = []
    # Calculate side lenghts
    for a, b, c in [coords_1, coords_2]:
        ab = sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
        bc = sqrt((c[0] - b[0])**2 + (c[1] - b[1])**2)
        ac = sqrt((c[0] - a[0])**2 + (c[1] - a[1])**2)
        sides.append(sorted([ab, bc, ac]))

    t1, t2 = sides
    # Ratio of side lengths must be the same
    return round(t1[0] / t2[0], 2) == round(t1[1] / t2[1], 2) == round(t1[2] / t2[2], 2)


if __name__ == '__main__':
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True   # 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False  # 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True   # 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True   # 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True   # 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False  # 'different #2'
    assert similar_triangles([[2, -1], [-2, -4], [1, -4]], [[5, -2], [-4, 1], [-4, 10]]) is True
    print("Coding complete")
