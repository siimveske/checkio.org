class MicrowaveBase:
    MAX_TIME = 90 * 60
    MIN_TIME = 0

    def __init__(self):
        self.time = 0

    def set_time(self, time: str):
        minutes, seconds = time.split(":")
        self.add_time(f"{minutes}m")
        self.add_time(f"{seconds}s")

    def add_time(self, time: str):
        time = self.parse_time(time)
        self.time = min(self.MAX_TIME, self.time + time)

    def del_time(self, time: str):
        time = self.parse_time(time)
        self.time = max(self.MIN_TIME, self.time - time)

    def parse_time(self, time: str) -> int:
        if "s" in time:
            time = int(time[:-1])
        else:
            time = int(time[:-1]) * 60
        return time


class Microwave1(MicrowaveBase):
    pass


class Microwave2(MicrowaveBase):
    pass


class Microwave3(MicrowaveBase):
    pass


class RemoteControl:
    def __init__(self, microwave: MicrowaveBase):
        self.microwave = microwave


if __name__ == '__main__':

    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")

    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")

    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:3_"
    assert remote_control_3.show_time() == "01:40"

    print("OK")
