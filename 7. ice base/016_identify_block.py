'''https://py.checkio.org/en/mission/identify-block/'''


def identify_block(numbers: set) -> str:
    """
    grid(4x4):
    +--+--+--+--+
    |1 |2 |3 |4 |
    +--+--+--+--+
    |5 |6 |7 |8 |
    +--+--+--+--+
    |9 |10|11|12|
    +--+--+--+--+
    |13|14|15|16|
    +--+--+--+--+


    blocks(7 kinds):

    'I'  'J'  'L'  'O'  'S'  'T'  'Z'

     *    *   *    **    **  ***  **
     *    *   *    **   **    *    **
     *   **   **
     *

    """

    # Possible block values if positioned to top left corner
    MAPPING = {
        'I': [{1, 2, 3, 4}, {1, 5, 9, 13}],
        'J': [{2, 6, 9, 10}, {1, 2, 3, 7}, {1, 2, 5, 9}, {1, 5, 6, 7}],
        'L': [{1, 5, 9, 10}, {3, 5, 6, 7}, {1, 2, 6, 10}, {1, 2, 3, 5}],
        'O': [{1, 2, 5, 6}],
        'S': [{2, 3, 5, 6}, {1, 5, 6, 10}],
        'Z': [{1, 2, 6, 7}, {2, 5, 6, 9}],
        'T': [{1, 2, 3, 6}, {1, 5, 6, 9}, {2, 5, 6, 7}, {2, 5, 6, 10}]
    }

    grid_size = 4
    min_row = float('inf')
    min_col = float('inf')
    block_cords = []

    # Calculate block coordinates
    for i in range(grid_size):
        for j in range(grid_size):
            value = (i * grid_size) + (j + 1)
            if value in numbers:
                min_row = min(min_row, i)
                min_col = min(min_col, j)
                block_cords.append((i, j))

    # Move block to top left corner and calculate it's values
    value = set()
    for r, c in block_cords:
        new_r = r - min_row
        new_c = c - min_col
        new_val = (new_r * grid_size) + (new_c + 1)
        value.add(new_val)

    for letter, values in MAPPING.items():
        if value in values:
            return letter

    return None


if __name__ == '__main__':

    assert identify_block({10, 13, 14, 15}) == 'T'
    assert identify_block({1, 5, 9, 6}) == 'T'
    assert identify_block({2, 3, 7, 11}) == 'L'
    assert identify_block({4, 8, 12, 16}) == 'I'
    assert identify_block({3, 1, 5, 8}) is None

    print('OK')
