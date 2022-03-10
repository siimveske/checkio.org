'''
https://py.checkio.org/en/mission/chunk/
'''

from typing import Iterable


def chunking_by(items: list, size: int) -> Iterable:
    chunks = []
    for i in range(0, len(items), size):
        chunks.append(items[i:i + size])
    return chunks


if __name__ == '__main__':
    assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
    assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
    assert list(chunking_by([5, 4], 7)) == [[5, 4]]
    assert list(chunking_by([], 3)) == []
    assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]

    print("OK")
