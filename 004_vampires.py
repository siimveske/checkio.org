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


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2


class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 50
        self.attack = 1


class Vampire(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 40
        self.attack = 4
        self.vampirism = 50


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


def fight(warrior1: Warrior, warrior2: Warrior):

    while warrior1.is_alive and warrior2.is_alive:
        defense = getattr(warrior2, 'defense', 0)
        if defense > warrior1.attack:
            continue
        else:
            dmg = (warrior1.attack - defense)
            warrior2.health -= dmg
            if type(warrior1) is Vampire:
                warrior1.health += (dmg * warrior1.vampirism) // 100

        if warrior2.is_alive:
            defense = getattr(warrior1, 'defense', 0)
            if defense > warrior2.attack:
                continue
            else:
                dmg = (warrior2.attack - defense)
                warrior1.health -= dmg
                if type(warrior2) is Vampire:
                    warrior2.health += (dmg * warrior2.vampirism) // 100

    return warrior1.is_alive


if __name__ == '__main__':

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True

    print("OK")
