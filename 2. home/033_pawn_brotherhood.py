"""
Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.
"""


def safe_pawns(pawns: set) -> int:
    cnt = 0
    for pawn in pawns:

        row = int(pawn[1])
        col = ord(pawn[0])

        defender1 = chr(col - 1) + str(row - 1)
        defender2 = chr(col + 1) + str(row - 1)

        if defender1 in pawns or defender2 in pawns:
            cnt += 1

    return cnt


if __name__ == '__main__':

    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

    print("OK")
