class HackerLanguage:
    def write(self, text):
        pass

    def delete(self, idx):
        pass

    def send(self):
        pass

    def read(self, text):
        pass


if __name__ == '__main__':

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"

    print("OK")
