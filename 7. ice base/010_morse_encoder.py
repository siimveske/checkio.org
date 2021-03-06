'''https://py.checkio.org/en/mission/morse-encoder/'''

MORSE = {'a': '.-', 'b': '-...', 'c': '-.-.',
         'd': '-..', 'e': '.', 'f': '..-.',
         'g': '--.', 'h': '....', 'i': '..',
         'j': '.---', 'k': '-.-', 'l': '.-..',
         'm': '--', 'n': '-.', 'o': '---',
         'p': '.--.', 'q': '--.-', 'r': '.-.',
         's': '...', 't': '-', 'u': '..-',
         'v': '...-', 'w': '.--', 'x': '-..-',
         'y': '-.--', 'z': '--..', '0': '-----',
         '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.'
         }


def morse_encoder(text: str) -> str:
    '''Solution from https://py.checkio.org/mission/morse-encoder/publications/igor.v.dudenko/python-3/translate/'''
    return ' '.join(text.lower()).translate(str.maketrans(MORSE))


if __name__ == '__main__':
    assert morse_encoder("some text") == "... --- -- .   - . -..- -"
    assert morse_encoder("2018") == "..--- ----- .---- ---.."
    assert morse_encoder("It was a good day") == ".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"
    print("OK")
