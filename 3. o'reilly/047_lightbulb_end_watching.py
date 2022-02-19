from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None) -> int:
    """
    how long the light bulb has been turned on
    """
    result = 0
    history = []

    for item in els:
        if not history:
            history.append(item)
            continue

        start = history.pop()
        stop = item

        if start_watching:
            if start_watching >= stop:
                continue
            if start < start_watching < stop:
                start = start_watching

        if end_watching:
            if end_watching <= start:
                continue
            if start < end_watching < stop:
                stop = end_watching

        result += (stop - start).total_seconds()

    if history:
        start = history.pop()
        if start >= end_watching:
            return int(result)

        stop = end_watching
        if start < start_watching < stop:
            start = start_watching

        result += (stop - start).total_seconds()

    return int(result)


if __name__ == '__main__':

    assert sum_light(els=[
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        start_watching=datetime(2015, 1, 12, 10, 0, 0),
        end_watching=datetime(2015, 1, 12, 10, 0, 10)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 7)) == 7

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 3),
        datetime(2015, 1, 12, 10, 0, 10)) == 7

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 10),
        datetime(2015, 1, 12, 10, 0, 20)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 10, 30, 0),
        datetime(2015, 1, 12, 11, 0, 0)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 10, 10, 0),
        datetime(2015, 1, 12, 11, 0, 0)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 10, 10, 0),
        datetime(2015, 1, 12, 11, 0, 10)) == 20

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 9, 50, 0),
        datetime(2015, 1, 12, 10, 0, 10)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 9, 0, 0),
        datetime(2015, 1, 12, 10, 5, 0)) == 300

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 11, 5, 0),
        datetime(2015, 1, 12, 12, 0, 0)) == 310

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
        datetime(2015, 1, 12, 11, 5, 0),
        datetime(2015, 1, 12, 11, 10, 0)) == 300

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
        datetime(2015, 1, 12, 10, 10, 0),
        datetime(2015, 1, 12, 11, 0, 10)) == 20

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 10, 0),
        datetime(2015, 1, 12, 10, 20, 20)) == 610

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 10, 0),
        datetime(2015, 1, 12, 10, 20, 20)) == 1220

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 9, 0),
        datetime(2015, 1, 12, 10, 0, 0)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 9, 0),
        datetime(2015, 1, 12, 10, 0, 10)) == 10

    print("OK")
