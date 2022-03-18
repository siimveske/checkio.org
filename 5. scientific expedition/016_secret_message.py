'''
https://py.checkio.org/en/mission/secret-message/
'''


def find_message(message: str) -> str:
    return ''.join([i for i in message if i.isupper()])


if __name__ == '__main__':
    assert find_message(('How are you? Eh, ok. Low or Lower? ' + 'Ohhh.')) == 'HELLO'
    assert find_message('hello world!') == ''
    assert find_message('HELLO WORLD!!!') == 'HELLOWORLD'
    print("OK")
