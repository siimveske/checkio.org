import math
from collections import defaultdict
from typing import List


def total_cost(calls: List[str]) -> int:
    mapping = defaultdict(int)
    for call in calls:
        date, time, duration = call.split(' ')
        mapping[date] += math.ceil(int(duration) / 60)

    total = 0
    for duration in mapping.values():
        expensive = max(0, duration - 100)
        cheap = duration - expensive
        cost = cheap + 2 * expensive
        total += cost

    return total


if __name__ == '__main__':
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
    print("OK")
