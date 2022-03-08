class Friend:
    def __init__(self, name):
        self.name = name
        self.invite = ""

    def show_invite(self) -> str:
        if self.invite:
            return self.invite
        else:
            return "No party..."


class Party:

    def __init__(self, place):
        self.place = place
        self.observers = set()

    def add_friend(self, friend: Friend):
        self.observers.add(friend)

    def del_friend(self, friend: Friend):
        try:
            self.observers.remove(friend)
        except KeyError:
            pass

    def send_invites(self, invite: str):
        for friend in self.observers:
            friend.invite = f"{self.place}: {invite}"


if __name__ == '__main__':

    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
    assert chuck.show_invite() == "No party..."

    print("OK")
