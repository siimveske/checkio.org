from typing import Tuple


def follow(instructions: str) -> Tuple[int, int]:

    mapper = {
        'f': lambda x, y: (x, y + 1),
        'b': lambda x, y: (x, y - 1),
        'l': lambda x, y: (x - 1, y),
        'r': lambda x, y: (x + 1, y)
    }

    result = (0, 0)
    for step in instructions:
        result = mapper[step](*result)

    return result


if __name__ == '__main__':
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("OK")
