from typing import List
from collections import deque


def letter_queue(commands: List[str]) -> str:
    queue = deque()
    for cmd in commands:
        if cmd == 'POP':
            if queue:
                queue.popleft()
        else:
            queue.append(cmd[-1])
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
