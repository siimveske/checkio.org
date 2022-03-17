from typing import List
from collections import deque


def letter_queue(commands: List[str]) -> str:
    queue = deque()
    for cmd in commands:
        if 'PUSH' in cmd:
            _, val = cmd.split()
            queue.append(val)
        else:
            if queue:
                queue.popleft()
    return ''.join(queue)


if __name__ == '__main__':
    assert letter_queue(['PUSH A',
                         'POP',
                         'POP',
                         'PUSH Z',
                         'PUSH D',
                         'PUSH O',
                         'POP',
                         'PUSH T']) == 'DOT'
    assert letter_queue(['POP', 'POP']) == ''
    assert letter_queue(['PUSH H', 'PUSH I']) == 'HI'
    assert letter_queue([]) == ''
    print("OK")
