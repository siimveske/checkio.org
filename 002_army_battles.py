from collections import deque


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


def fight(warrior1: Warrior, warrior2: Warrior):

    while warrior1.is_alive and warrior2.is_alive:
        warrior2.health -= warrior1.attack
        if warrior2.is_alive:
            warrior1.health -= warrior2.attack

    return warrior1.is_alive


class Army:
    def __init__(self) -> None:
        self.units = deque()

    def add_units(self, unit_type: Warrior, count: int):
        for i in range(count):
            self.units.append(unit_type())


class Battle:
    def fight(self, army1: Army, army2: Army):
        unit1: Warrior = army1.units.popleft()
        unit2: Warrior = army2.units.popleft()
        while unit1 and unit2:
            try:
                if fight(unit1, unit2):
                    unit2 = army2.units.popleft()
                else:
                    unit1 = army1.units.popleft()
            except IndexError:
                break

        return unit1.is_alive


if __name__ == '__main__':

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("OK")
