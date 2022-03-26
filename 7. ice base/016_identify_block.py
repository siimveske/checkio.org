'''https://py.checkio.org/en/mission/identify-block/'''


def identify_block(numbers):
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
    return None


if __name__ == '__main__':

    assert identify_block({10, 13, 14, 15}) == 'T'
    assert identify_block({1, 5, 9, 6}) == 'T'
    assert identify_block({2, 3, 7, 11}) == 'L'
    assert identify_block({4, 8, 12, 16}) == 'I'
    assert identify_block({3, 1, 5, 8}) is None

    print('OK')
