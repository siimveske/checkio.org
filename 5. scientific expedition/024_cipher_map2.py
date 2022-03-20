'''
https://py.checkio.org/en/mission/cipher-map2/
'''
from typing import List


def recall_password(grille: List[str], password: List[str]) -> str:
    # your code here
    return None


if __name__ == '__main__':
    assert recall_password(['X...', '..X.', 'X..X', '....'],
                           ['itdf', 'gdce', 'aton', 'qrdi']) == 'icantforgetiddqd'
    assert recall_password(['....', 'X..X', '.X..', '...X'],
                           ['xhwc', 'rsqx', 'xqzz', 'fyzr']) == 'rxqrwsfzxqxzhczy'
    print("OK")
