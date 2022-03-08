class Lamp:
    def __init__(self) -> None:
        self.idx = 0
        self.colors = ["Green", "Red", "Blue", "Yellow"]

    def light(self) -> str:
        color = self.colors[self.idx]
        self.idx = (self.idx + 1) % len(self.colors)
        return color


if __name__ == '__main__':

    lamp_1 = Lamp()
    lamp_2 = Lamp()

    lamp_1.light()  # Green
    lamp_1.light()  # Red
    lamp_2.light()  # Green

    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"

    print("OK")
