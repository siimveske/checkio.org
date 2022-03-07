class HackerLanguage:
    def __init__(self):
        self.text = []

    def write(self, text):
        for i in text:
            self.text.append(i)

    def delete(self, idx):
        self.text = self.text[0:-idx]

    def send(self):
        buffer = []
        for i in self.text:
            if i == ' ':
                buffer.append('1000000')
            elif i.isalpha():
                buffer.append(bin(ord(i))[2:])
            else:
                buffer.append(i)
        return ''.join(buffer)

    def read(self, text):
        buffer = []
        parts = text.split('1000000')
        for part in parts:
            idx = 0
            step = 7
            while idx < len(part):
                slice = part[idx:idx + step]
                try:
                    letter = chr(int(slice, 2))
                    buffer.append(letter)
                    idx += step
                except ValueError:
                    buffer.append(part[idx])
                    idx += 1
            buffer.append(' ')
        return ''.join(buffer).strip()


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
