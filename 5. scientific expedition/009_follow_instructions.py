from typing import Tuple


def follow(instructions: str) -> Tuple[int, int]:

    mapper = {
        'f': (0, 1),
        'b': (0, -1),
        'r': (1, 0),
        'l': (-1, 0),
    }

    x, y = (0, 0)
    for i in instructions:
        dx, dy = mapper[i]
        x += dx
        y += dy

    return (x, y)


if __name__ == '__main__':
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("OK")
