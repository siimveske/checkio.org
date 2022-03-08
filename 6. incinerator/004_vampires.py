from collections import deque


class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0

    def calculate_damage(self, damage: int) -> int:
        return damage

    def decrease_health(self, damage: int):
        self.health -= self.calculate_damage(damage)

    def hit(self, victim):
        victim.decrease_health(self.attack)


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3)
        self.defense = 2

    def calculate_damage(self, damage):
        return max(0, damage - self.defense)


class Vampire(Warrior):
    def __init__(self):
        super().__init__(health=40, attack=4)
        self.vampirism = 0.5

    def hit(self, victim: Warrior):
        super().hit(victim)
        self.health += int(victim.calculate_damage(self.attack) * self.vampirism)


class Rookie(Warrior):
    def __init__(self):
        super().__init__(health=50, attack=1)


def fight(unit_1: Warrior, unit_2: Warrior) -> bool:
    attacker, victim = unit_1, unit_2
    while (attacker.is_alive and victim.is_alive):
        attacker.hit(victim)
        victim, attacker = attacker, victim
    return unit_1.is_alive


class Army:
    def __init__(self) -> None:
        self.units = deque()

    def add_units(self, unit: Warrior, count: int):
        for _ in range(count):
            self.units.append(unit())

    @property
    def is_alive(self) -> bool:
        """Does the army have a living warrior?"""
        return len(self.units) > 0

    @property
    def warrior(self) -> Warrior:
        """Return first alive warrior"""
        return self.units[0] if self.units else None

    def pop_dead(self):
        """Pop a dead warrior out of the list."""
        self.units.popleft()


class Battle:
    def fight(self, army_1: Army, army_2: Army):
        while army_1.is_alive and army_2.is_alive:
            if fight(army_1.warrior, army_2.warrior):
                army_2.pop_dead()
            else:
                army_1.pop_dead()
        return army_1.is_alive


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
