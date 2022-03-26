'''https://py.checkio.org/en/mission/the-cheapest-flight/'''

from collections import defaultdict


def build_graph(costs: list) -> dict:
    graph = defaultdict(list)
    for flight in costs:
        a, b, cost = flight
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    return graph


def travel(graph: dict, start: str, destination: str, visited: set) -> int:
    if start == destination:
        return 0

    visited.add(start)

    min_cost = float('inf')
    for neighbor in graph[start]:
        city, cost = neighbor
        if city in visited:
            continue
        price = cost + travel(graph, city, destination, visited)
        min_cost = min(min_cost, price)

    return min_cost


def cheapest_flight(costs: list, a: str, b: str) -> int:
    graph = build_graph(costs)
    cost = travel(graph, a, b, set())
    if cost == float('inf'):
        return 0
    else:
        return cost


if __name__ == '__main__':

    assert cheapest_flight([['A', 'C', 100],
                            ['A', 'B', 20],
                            ['B', 'C', 50]],
                           'A',
                           'C') == 70
    assert cheapest_flight([['A', 'C', 100],
                            ['A', 'B', 20],
                            ['B', 'C', 50]],
                           'C',
                           'A') == 70
    assert cheapest_flight([['A', 'C', 40],
                            ['A', 'B', 20],
                            ['A', 'D', 20],
                            ['B', 'C', 50],
                            ['D', 'C', 70]],
                           'D',
                           'C') == 60
    assert cheapest_flight([['A', 'C', 100],
                            ['A', 'B', 20],
                            ['D', 'F', 900]],
                           'A',
                           'F') == 0
    assert cheapest_flight([['A', 'B', 10],
                            ['A', 'C', 15],
                            ['B', 'D', 15],
                            ['C', 'D', 10]],
                           'A',
                           'D') == 25

    print("OK")
