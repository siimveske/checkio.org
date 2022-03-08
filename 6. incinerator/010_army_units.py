class Army:

    def __init__(self):
        self.army_type: str = ""

    def train_swordsman(self, name: str):
        raise NotImplementedError()

    def train_lancer(self, name: str):
        raise NotImplementedError()

    def train_archer(self, name: str):
        raise NotImplementedError()


class Warrior:

    def __init__(self, name, warrior_type, army_type):
        self.name = name
        self.warrior_type = warrior_type
        self.army_type = army_type
        self.specialization = self.__class__.__name__.lower()

    def introduce(self):
        return f"{self.warrior_type} {self.name}, {self.army_type} {self.specialization}"


class Swordsman(Warrior):
    ...


class Lancer(Warrior):
    ...


class Archer(Warrior):
    ...


class AsianArmy(Army):

    def __init__(self):
        self.army_type = "Asian"

    def train_swordsman(self, name):
        return Swordsman(name, "Samurai", self.army_type)

    def train_lancer(self, name):
        return Lancer(name, "Ronin", self.army_type)

    def train_archer(self, name):
        return Archer(name, "Shinobi", self.army_type)


class EuropeanArmy(Army):

    def __init__(self):
        self.army_type = "European"

    def train_swordsman(self, name):
        return Swordsman(name, "Knight", self.army_type)

    def train_lancer(self, name):
        return Lancer(name, "Raubritter", self.army_type)

    def train_archer(self, name):
        return Archer(name, "Ranger", self.army_type)


if __name__ == '__main__':

    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"

    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"

    print("OK")
