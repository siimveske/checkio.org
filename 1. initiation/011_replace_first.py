from typing import Iterable


def replace_first(items: list) -> Iterable:
    """In a given list the first element should become the last one.
    An empty list or list with only one element should stay the same."""
    return items[1:] + items[:1]


if __name__ == "__main__":

    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []

    print("OK")
