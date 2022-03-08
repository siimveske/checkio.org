class Text:
    def __init__(self):
        self.text = ""
        self.font = ""

    def write(self, text: str):
        self.text += text

    def set_font(self, font: str):
        self.font = f'[{font}]'

    def show(self):
        return f"{self.font}{self.text}{self.font}"

    def restore(self, commit: tuple):
        self.font, self.text = commit


class SavedText:
    def __init__(self):
        self.repo = dict()
        self.version = 0

    def save_text(self, text: Text):
        self.repo[self.version] = (text.font, ''.join(text.text))
        self.version += 1

    def get_version(self, number: int):
        font, text = self.repo.get(number)
        return (font, ''.join(text))


if __name__ == '__main__':

    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("OK")
