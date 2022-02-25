def checkio(text: str, word: str):
    puzzle = []
    for line in text.splitlines():
        puzzle.append(line.replace(' ', '').lower())

    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == word[0]:
                row, col = [], []
                for k in range(len(word)):
                    try:
                        row.append(puzzle[i][j + k])
                    except IndexError:
                        pass
                    try:
                        col.append(puzzle[i + k][j])
                    except IndexError:
                        pass
                if ''.join(row) == word:
                    return [i + 1, j + 1, i + 1, j + len(word)]
                if ''.join(col) == word:
                    return [i + 1, j + 1, i + len(word), j + 1]


if __name__ == '__main__':
    assert checkio(
        """DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio(
        """He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]

print("OK")
