'''
https://py.checkio.org/en/mission/cipher-crossword/
'''


def checkio(crossword: list, words: list):
    board = crossword[::2] + [i for i in zip(*crossword)][::2]
    solution = {0: ' '}

    def solve(words: list, memo: dict):
        if words:
            codes = board[len(words) - 1]
            for word in words:
                new_memo = memo.copy()
                flag = True
                for letter, current_code in zip(word, codes):
                    solution[current_code] = letter
                    previous_code = memo.get(letter)
                    if previous_code:
                        if (flag := previous_code == current_code) is False:
                            break
                    else:
                        new_memo[letter] = current_code
                if flag and solve([w for w in words if w != word], new_memo):
                    return True
            return False
        else:
            return True

    solve(words, {})
    return [[solution[num] for num in row] for row in crossword]


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
