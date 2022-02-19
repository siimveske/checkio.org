from typing import List
import statistics


def checkio(data: List[int]):
    return statistics.median(data)


if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3
    assert checkio([3, 1, 2, 5, 3]) == 3
    assert checkio([1, 300, 2, 200, 1]) == 2
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5
    print("OK")
