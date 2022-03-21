'''https://py.checkio.org/en/mission/count-chains/'''

import math
from typing import List, Tuple


def distance(a: Tuple[int, int], b: Tuple[int, int]) -> float:
    x1, y1 = a
    x2, y2 = b
    return math.hypot(x2 - x1, y2 - y1)


def intersect(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> bool:
    x1, y1, r1 = a
    x2, y2, r2 = b
    dist = distance((x1, y1), (x2, y2))
    return abs(r2 - r1) < dist < (r1 + r2)


def mark_visited(graph: dict, start: Tuple[int, int, int], visited: dict):
    visited.add(start)
    for node in graph[start]:
        if node not in visited:
            mark_visited(graph, node, visited)


def build_graph(circles: list) -> dict:
    graph = {c: [] for c in circles}
    for i in range(len(circles) - 1):
        for j in range(i + 1, len(circles)):
            a, b = circles[i], circles[j]
            if intersect(a, b):
                graph[a].append(b)
                graph[b].append(a)
    return graph


def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    graph = build_graph(circles)

    cnt, visited = 0, set()
    for circle in graph:
        if circle not in visited:
            mark_visited(graph, circle, visited)
            cnt += 1
    return cnt


if __name__ == '__main__':
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'

    # Basics/6
    assert count_chains([(1, 3, 1), (2, 2, 1), (4, 2, 1), (5, 3, 1), (3, 3, 1)]) == 1

    print("OK")
