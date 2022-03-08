class VoiceCommand:
    def __init__(self, channels) -> None:
        self.channels = channels
        self.active_channel = 0

    def first_channel(self):
        self.active_channel = 0
        return self.current_channel()

    def last_channel(self):
        self.active_channel = len(self.channels) - 1
        return self.current_channel()

    def turn_channel(self, n):
        self.active_channel = n - 1
        return self.current_channel()

    def next_channel(self):
        self.active_channel = (self.active_channel + 1) % len(self.channels)
        return self.current_channel()

    def previous_channel(self):
        self.active_channel = (self.active_channel - 1) % len(self.channels)
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.active_channel]

    def is_exist(self, channel):
        if type(channel) is int:
            return "Yes" if 0 < channel <= len(self.channels) else "No"
        else:
            return "Yes" if channel in self.channels else "No"


if __name__ == '__main__':

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)

    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"

    print("OK")
