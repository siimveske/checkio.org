'''
You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits. The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).
'''
from typing import List


def checkio(matrix: List[List[int]]) -> bool:
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            cnt = explore(matrix, x, y)
            if cnt >= 4:
                return True
    return False


def explore(matrix, x, y):
    neighbors = dict(
        up=(-1, 0),
        up_right=(-1, 1),
        right=(0, 1),
        down_right=(1, 1),
        down=(1, 0),
        down_left=(1, -1),
        left=(0, -1),
        up_left=(1, -1)
    )

    result = float('-inf')
    current_value = matrix[x][y]

    for dx, dy in neighbors.values():
        cnt = 1
        nx, ny = x + dx, y + dy

        while inbound(matrix, nx, ny) and matrix[nx][ny] == current_value:
            cnt += 1
            nx, ny = nx + dx, ny + dy

        result = max(cnt, result)
        if result >= 4:
            break

    return cnt


def inbound(matrix, x, y):
    row_inbound = 0 <= x < len(matrix)
    col_inbound = 0 <= y < len(matrix[0])
    return row_inbound and col_inbound


if __name__ == '__main__':
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True
    print('All Done! Time to check!')
