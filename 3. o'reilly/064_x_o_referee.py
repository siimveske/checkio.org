from typing import List


def checkio(game_result: List[str]) -> str:
    di1, di2 = [], []
    resmap = {'XXX': 'X', 'OOO': 'O'}
    board_size = 3

    for i in range(board_size):
        row, col = [], []
        for j in range(board_size):
            row.append(game_result[i][j])
            col.append(game_result[j][i])

        row = ''.join(row)
        col = ''.join(col)
        if row in resmap:
            return resmap[row]
        elif col in resmap:
            return resmap[col]
        else:
            di1.append(game_result[i][i])
            di2.append(game_result[i][2 - i])

    di1 = ''.join(di1)
    di2 = ''.join(di2)
    if di1 in resmap:
        return resmap[di1]
    elif di2 in resmap:
        return resmap[di2]
    else:
        return 'D'

    # [
    #     [(0,0),(0,1),(0,2)],
    #     [(1,0),(1,1),(1,2)],
    #     [(2,0),(2,1),(2,2)],

    #     [(0,0),(1,0),(2,0)],
    #     [(0,1),(1,1),(2,1)],
    #     [(0,2),(1,2),(2,2)],

    #     [(0,0),(1,1),(2,2)],
    #     [(0,2),(1,1),(2,0)],
    # ]


if __name__ == "__main__":
    assert checkio(["X.O", "XX.", "XOO"]) == "X", "X wins"
    assert checkio(["OO.", "XOX", "XOX"]) == "O", "O wins"
    assert checkio(["OOX", "XXO", "OXX"]) == "D", "Draw"
    assert checkio(["O.X", "XX.", "XOO"]) == "X", "X wins again"
