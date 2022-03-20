'''
https://py.checkio.org/en/mission/cipher-map2/
'''
from typing import List


def transpose(matrix) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]


def reflect(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


def rotate(matrix: List[List[object]]) -> None:
    '''Reverse on Diagonal and then Reverse Left to Right
    https://leetcode.com/problems/rotate-image/solution/'''
    transpose(matrix)
    reflect(matrix)


def get_symbols(matrix: List[List[object]], password: List[str]) -> str:
    symbols = []
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'X':
                symbols.append(password[i][j])
    return ''.join(symbols)


def recall_password(grille: List[str], password: List[str]) -> str:
    code = []
    matrix = [list(row) for row in grille]
    for _ in range(4):
        symbols = get_symbols(matrix, password)
        code.append(symbols)
        rotate(matrix)
    return ''.join(code)


if __name__ == '__main__':
    assert recall_password(['X...', '..X.', 'X..X', '....'],
                           ['itdf', 'gdce', 'aton', 'qrdi']) == 'icantforgetiddqd'
    assert recall_password(['....', 'X..X', '.X..', '...X'],
                           ['xhwc', 'rsqx', 'xqzz', 'fyzr']) == 'rxqrwsfzxqxzhczy'
    print("OK")
