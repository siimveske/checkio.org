import copy


class Text:
    def __init__(self):
        self.text = []
        self.font = ""

    def write(self, text: str):
        self.text.append(text)

    def set_font(self, font: str):
        self.font = font

    def show(self):
        if self.font:
            return f"[{self.font}]{''.join(self.text)}[{self.font}]"
        else:
            return ''.join(self.text)

    def restore(self, commit: tuple):
        font, text = commit
        self.font = font
        self.text = text


class SavedText:
    def __init__(self):
        self.repo = dict()
        self.version = 0

    def save_text(self, text: Text):
        self.repo[self.version] = (text.font, copy.deepcopy(text.text))
        self.version += 1

    def get_version(self, number: int):
        font, text = self.repo.get(number)
        return (font, copy.deepcopy(text))


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
