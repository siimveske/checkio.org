'''https://py.checkio.org/en/mission/the-cheapest-flight/'''
from typing import List


def cheapest_flight(costs: List, a: str, b: str) -> int:
    return None


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
