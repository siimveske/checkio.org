'''
You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits. The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).
'''
from typing import List


def checkio(matrix: List[List[int]]) -> bool:
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            cnt = dfs(matrix, x, y, set())
            if cnt >= 4:
                return True
    return False


def dfs(matrix, x, y, visited):

    location = (x, y)
    if location in visited:
        return 0
    visited.add(location)

    cnt = 1
    current_value = matrix[x][y]

    for nx, ny in get_neighbors(matrix, x, y, current_value):
        if (nx, ny) not in visited:
            cnt += dfs(matrix, nx, ny, set(visited))

    return cnt


def get_neighbors(matrix, x, y, value):

    neighbors = dict(
        up=(x - 1, y),
        up_right=(x - 1, y + 1),
        right=(x, y + 1),
        down_right=(x + 1, y + 1),
        down=(x + 1, y),
        down_left=(x + 1, y - 1),
        left=(x, y - 1),
        up_left=(x + 1, y - 1)
    )

    result = []
    for nx, ny in neighbors.values():

        row_inbound = 0 <= nx < len(matrix)
        col_inbound = 0 <= ny < len(matrix[0])

        if row_inbound and col_inbound and matrix[nx][ny] == value:
            result.append((nx, ny))

    return result


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
