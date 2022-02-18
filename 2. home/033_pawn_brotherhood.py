"""
Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.
"""


def safe_pawns(pawns: set) -> int:
    num_to_letter = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
    letter_to_num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    cnt = 0

    for pawn in pawns:

        row = int(pawn[1])
        col = letter_to_num[pawn[0]]

        location1 = f'{num_to_letter.get(col - 1, -1)}{row - 1}'
        location2 = f'{num_to_letter.get(col + 1, -1)}{row - 1}'

        if location1 in pawns or location2 in pawns:
            cnt += 1

    return cnt


if __name__ == '__main__':

    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

    print("OK")
