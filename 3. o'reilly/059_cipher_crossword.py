'''
https://py.checkio.org/en/mission/cipher-crossword/
'''
from collections import defaultdict


def checkio(crossword, words):

    rules = defaultdict(str)
    r = solve(crossword, words, rules)
    result = [
        [i for i in r[0]],
        [r[3][1], ' ', r[5][1], ' ', r[1][1]],
        [i for i in r[4]],
        [r[3][3], ' ', r[5][3], ' ', r[1][3]],
        [i for i in r[2]]
    ]
    return result


def scan(crossword, words, rules, coords):

    solution = []
    r, c = coords

    for word_idx, word in enumerate(words):
        new_rules = rules.copy()
        problem = False
        for char_idx, char in enumerate(word):
            row = char_idx if r is None else r
            col = char_idx if c is None else c
            constraint = crossword[row][col]
            if new_rules.setdefault(constraint, char) != char:
                problem = True
                break  # character already used
            new_rules[constraint] = char

        if problem:
            continue

        remainder = words[:word_idx] + words[word_idx + 1:]
        if remainder == []:
            solution = [word]
            break

        r = solve(crossword, remainder, new_rules)
        if r:
            solution = [word] + r
            break

    return solution


def solve(crossword, words, rules):

    solution = []

    if len(words) == 6:  # Solve top row
        coords = (0, None)  # Scan top row from left to right
        solution = scan(crossword, words, rules, coords)

    elif len(words) == 5:  # Solve right column
        coords = (None, 4)  # Scan right column from top to bottom
        solution = scan(crossword, words, rules, coords)

    elif len(words) == 4:  # Solve bottom row
        coords = (4, None)  # # Scan bottom row from left to right
        solution = scan(crossword, words, rules, coords)

    elif len(words) == 3:  # Solve left column
        coords = (None, 0)  # Scan left column top to bottom
        solution = scan(crossword, words, rules, coords)

    elif len(words) == 2:  # Solve middle row
        coords = (2, None)  # Scan middle row from left to right
        solution = scan(crossword, words, rules, coords)

    else:  # Solve middle column (last one)
        coords = (None, 2)  # Scan middle column from top to bottomt
        solution = scan(crossword, words, rules, coords)

    return solution


if __name__ == "__main__":
    assert checkio(
        [
            [21, 6, 25, 25, 17],
            [14, 0, 6, 0, 2],
            [1, 11, 16, 1, 17],
            [11, 0, 16, 0, 5],
            [26, 3, 14, 20, 6],
        ],
        ["hello", "habit", "lemma", "ozone", "bimbo", "trace"],
    ) == [
        ["h", "e", "l", "l", "o"],
        ["a", " ", "e", " ", "z"],
        ["b", "i", "m", "b", "o"],
        ["i", " ", "m", " ", "n"],
        ["t", "r", "a", "c", "e"],
    ]

    print('OK')
