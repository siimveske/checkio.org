import re


class HackerLanguage:
    def __init__(self):
        self.text = []

    def write(self, text):
        for i in text:
            self.text.append(i)

    def delete(self, idx):
        self.text = self.text[:-idx]

    def send(self):
        buffer = []
        for i in self.text:
            if i == ' ':
                buffer.append('1000000')
            elif i.isalpha():
                buffer.append(format(ord(i), 'b'))
            else:
                buffer.append(i)
        return ''.join(buffer)

    def convert(self, matchobj):
        code = matchobj[0]
        return chr(int(code, 2)) if code != '1000000' else ' '

    def read(self, text):
        return re.sub(r'[01]{7}', self.convert, text)


if __name__ == '__main__':

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")

    assert message_1.send() == "111001111001011100011111001011001011110100"

    message_1 = HackerLanguage()
    message_1.write('Remember: 21.07.2018 at 11:11AM')
    message_1.delete(2)
    message_1.write('PM')
    message_1.send() == '10100101100101110110111001011101101110001011001011110010:100000021.07.2018100000011000011110100100000011:1110100001001101'

    message_2 = HackerLanguage()
    assert message_2.read("11001011101101110000111010011101100") == "email"

    message_2 = HackerLanguage()
    message_2.read('10011011111001100000011001011101101110000111010011101100100000011010011110011100000011011011110010.11100101101111110001011011111110100@11001111101101110000111010011101100.110001111011111101101') == 'My email is mr.robot@gmail.com'

    print("OK")
