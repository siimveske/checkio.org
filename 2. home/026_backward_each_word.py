'''
In a given string you should reverse every word, but the words should stay in their places.
'''


def backward_string_by_word(text: str) -> str:

    result = []
    words = text.split(' ')

    if not words:
        return text[::-1]

    for word in words:
        result.append(word[::-1])

    result = ' '.join(result)
    return result


if __name__ == '__main__':

    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'

    print("OK")
