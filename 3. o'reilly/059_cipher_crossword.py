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


def solve(crossword, words, rules):

    solution = []

    if len(words) == 6:  # Solve First Row
        for word_idx, word in enumerate(words):
            new_rules = rules.copy()
            problem = False
            for char_idx, char in enumerate(word):
                constraint = crossword[0][char_idx]  # scan top row from left to right
                if constraint in new_rules and new_rules[constraint] != char:
                    problem = True
                    break  # we have already used a different character
                new_rules[constraint] = char

            if problem:
                continue

            remainder = words[:word_idx] + words[word_idx + 1:]
            if remainder == []:
                break

            r = solve(crossword, remainder, new_rules)
            if r:
                solution = [word] + r
                break

    elif len(words) == 5:  # Solve right column
        for word_idx, word in enumerate(words):
            new_rules = rules.copy()
            problem = False
            for char_idx, char in enumerate(word):
                constraint = crossword[char_idx][4]  # scan right column from top to bottom
                if constraint in new_rules and new_rules[constraint] != char:
                    problem = True
                    break  # we have already used a different character
                new_rules[constraint] = char
            if problem:
                continue

            remainder = words[:word_idx] + words[word_idx + 1:]
            if remainder == []:
                break

            r = solve(crossword, remainder, new_rules)
            if r:
                solution = [word] + r
                break

    elif len(words) == 4:  # Solve last row
        for word_idx, word in enumerate(words):
            new_rules = rules.copy()
            problem = False
            for char_idx, char in enumerate(word):
                constraint = crossword[4][char_idx]  # scan bottom row
                if constraint in new_rules and new_rules[constraint] != char:
                    problem = True
                    break  # we have already used a different character
                new_rules[constraint] = char

            if problem:
                continue

            remainder = words[:word_idx] + words[word_idx + 1:]
            if remainder == []:
                break

            r = solve(crossword, remainder, new_rules)
            if r:
                solution = [word] + r
                break

    elif len(words) == 3:  # Solve left column
        for word_idx, word in enumerate(words):
            new_rules = rules.copy()
            problem = False
            for char_idx, char in enumerate(word):
                constraint = crossword[char_idx][0]  # scan left column
                if constraint in new_rules and new_rules[constraint] != char:
                    problem = True
                    break  # we have already used a different character
                new_rules[constraint] = char

            if problem:
                continue

            remainder = words[:word_idx] + words[word_idx + 1:]
            if remainder == []:
                break

            r = solve(crossword, remainder, new_rules)
            if r:
                solution = [word] + r
                break

    elif len(words) == 2:  # Solve middle row
        for word_idx, word in enumerate(words):
            new_rules = rules.copy()
            problem = False
            for char_idx, char in enumerate(word):
                constraint = crossword[2][char_idx]  # scan middle row from left to right
                if constraint in new_rules and new_rules[constraint] != char:
                    problem = True
                    break  # we have already used a different character
                new_rules[constraint] = char

            if problem:
                continue

            remainder = words[:word_idx] + words[word_idx + 1:]
            if remainder == []:
                break

            r = solve(crossword, remainder, new_rules)
            if r:
                solution = [word] + r
                break
    else:  # Solve middle column (last one to be solved)
        word = words[0]
        new_rules = rules.copy()
        problem = False
        for char_idx, char in enumerate(word):
            constraint = crossword[char_idx][2]  # scan middle column from top to bottom
            if constraint in new_rules and new_rules[constraint] != char:
                problem = True
                break  # we have already used a different character
            new_rules[constraint] = char

        if not problem:
            solution = [word]

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
