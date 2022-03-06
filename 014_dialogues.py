VOWELS = "aeiou"


class User:
    def __init__(self, name: str):
        self.name: str = name
        self.terminal: Chat = None

    def send(self, text: str):
        self.terminal.history.append((self.name, text))


class Chat:
    def __init__(self):
        self.history = []

    def connect_user(self, user: User):
        user.terminal = self

    def connect_human(self, human: User):
        self.connect_user(human)

    def connect_robot(self, robot: User):
        self.connect_user(robot)

    def show_human_dialogue(self) -> str:
        out = []
        for name, text in self.history:
            out.append(f"{name} said: {text}")
        return "\n".join(out)

    def show_robot_dialogue(self) -> str:
        out = []
        for name, text in self.history:
            bin_text = "".join(["0" if i in VOWELS else "1" for i in text])
            out.append(f"{name} said: {bin_text}")
        return "\n".join(out)


class Human(User):
    ...


class Robot(User):
    ...


if __name__ == "__main__":

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

    print("OK")
