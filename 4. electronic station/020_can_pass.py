def can_pass(matrix, first, second):

    visited = set()
    stack = [first]
    value = matrix[first[0]][first[1]]

    while stack:
        r, c = stack.pop()

        if (r, c) in visited:
            continue
        if not inbounds(matrix, r, c):
            continue
        if matrix[r][c] != value:
            continue

        if (r, c) == second:
            return True

        visited.add((r, c))
        for x, y in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            stack.append((r + x, c + y))

    return False


def inbounds(matrix, r, c):
    in_row_bounds = 0 <= r < len(matrix)
    in_col_bounds = 0 <= c < len(matrix[0])
    return in_row_bounds and in_col_bounds


if __name__ == '__main__':
    # assert can_pass(((0, 0, 0, 0, 0, 0),
    #                  (0, 2, 2, 2, 3, 2),
    #                  (0, 2, 0, 0, 0, 2),
    #                  (0, 2, 0, 2, 0, 2),
    #                  (0, 2, 2, 2, 0, 2),
    #                  (0, 0, 0, 0, 0, 2),
    #                  (2, 2, 2, 2, 2, 2),),
    #                 (3, 2), (0, 5)) == True

    # assert can_pass(((0, 0, 0, 0, 0, 0),
    #                  (0, 2, 2, 2, 3, 2),
    #                  (0, 2, 0, 0, 0, 2),
    #                  (0, 2, 0, 2, 0, 2),
    #                  (0, 2, 2, 2, 0, 2),
    #                  (0, 0, 0, 0, 0, 2),
    #                  (2, 2, 2, 2, 2, 2),),
    #                 (3, 3), (6, 0)) == False

    assert can_pass(((0, 0),
                     (0, 0)),
                    (0, 0), (1, 1)) == True
