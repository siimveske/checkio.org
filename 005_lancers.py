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


class Lancer(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 50
        self.attack = 6


class Army:
    def __init__(self) -> None:
        self.units = deque()

    def add_units(self, unit_type: Warrior, count: int):
        for i in range(count):
            self.units.append(unit_type())


class Battle:
    def fight(self, army1: Army, army2: Army):
        unit11: Warrior = army1.units.popleft()
        unit12 = None
        unit21: Warrior = army2.units.popleft()
        unit22 = None
        while unit11 and unit21:
            try:
                if type(unit11) is Lancer and len(army2.units) > 0:
                    unit22 = army2.units[0]
                if type(unit21) is Lancer and len(army1.units) > 0:
                    unit12 = army1.units[0]

                if fight([unit11, unit12], [unit21, unit22]):
                    unit21 = army2.units.popleft()
                else:
                    unit11 = army1.units.popleft()
            except IndexError:
                break

        return unit11.is_alive


def fight(warrior1, warrior2):

    warrior12, warrior22 = None, None
    if type(warrior1) is list:
        warrior1, warrior12 = warrior1
    if type(warrior2) is list:
        warrior2, warrior22 = warrior2

    while warrior1.is_alive and warrior2.is_alive:
        defense = getattr(warrior2, 'defense', 0)
        if defense > warrior1.attack:
            continue
        else:
            dmg = (warrior1.attack - defense)
            warrior2.health -= dmg
            if type(warrior1) is Vampire:
                warrior1.health += (dmg * warrior1.vampirism) // 100
            if type(warrior1) is Lancer and warrior22 is not None:
                warrior22.health -= int(dmg * 0.5)

        if warrior2.is_alive:
            defense = getattr(warrior1, 'defense', 0)
            if defense > warrior2.attack:
                continue
            else:
                dmg = (warrior2.attack - defense)
                warrior1.health -= dmg
                if type(warrior2) is Vampire:
                    warrior2.health += (dmg * warrior2.vampirism) // 100
                if type(warrior2) is Lancer and warrior12 is not None:
                    warrior12.health -= int(dmg * 0.5)

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
    freelancer = Lancer()
    vampire = Vampire()

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
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False

    # Battle test 2
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Lancer, 7)
    army_1.add_units(Vampire, 3)
    army_1.add_units(Warrior, 4)
    army_1.add_units(Defender, 2)
    army_2.add_units(Warrior, 4)
    army_2.add_units(Defender, 4)
    army_2.add_units(Vampire, 6)
    army_2.add_units(Lancer, 4)
    battle = Battle()
    battle.fight(army_1, army_2)

    print("OK")
