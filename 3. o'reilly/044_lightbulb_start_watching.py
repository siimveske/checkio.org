from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    """
    how long the light bulb has been turned on
    """
    result = 0

    for start, stop in zip(els[::2], els[1::2]):
        time = max(start_watching or stop, stop) - max(start_watching or start, start)
        result += time.total_seconds()

    return int(result)


if __name__ == '__main__':

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 5),
        ) == 5
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
        ) == 10
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 0),
        ) == 610
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 10),
        ) == 600
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
        ) == 620
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 11),
                datetime(2015, 1, 12, 12, 10, 11),
            ],
            datetime(2015, 1, 12, 12, 10, 11),
        ) == 0
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 11),
                datetime(2015, 1, 12, 12, 10, 11),
            ],
            datetime(2015, 1, 12, 12, 9, 11),
        ) == 60
    )

    print("OK")
