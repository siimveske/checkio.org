from collections import deque


class Warrior:
    def __init__(self, health=50, attack=5, army=None):
        self._max_health = health
        self.health = health
        self.attack = attack
        self.army = army

    @property
    def is_alive(self):
        return self.health > 0

    def calculate_damage(self, damage: int) -> int:
        return damage

    def decrease_health(self, amount: int):
        self.health = max(0, self.health - amount)

    def increase_health(self, amount: int):
        self.health = min(self._max_health, self.health + amount)

    def hit(self, victim):
        damage = victim.calculate_damage(self.attack)
        victim.decrease_health(damage)

        if self.army:
            next_warrior = self.army.next_warrior(self)
            if type(next_warrior) is Healer:
                next_warrior.heal(self)

        return damage


class Knight(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(attack=7, *args, **kwargs)
        self.attack = 7


class Defender(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(health=60, attack=3, *args, **kwargs)
        self.defense = 2

    def calculate_damage(self, damage):
        return max(0, damage - self.defense)


class Vampire(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(health=40, attack=4, *args, **kwargs)
        self.vampirism = 0.5

    def hit(self, victim: Warrior):
        damage = super().hit(victim)
        health = int(damage * self.vampirism)
        self.increase_health(health)


class Lancer(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(attack=6, *args, **kwargs)
        self.splash = int(self.attack * 0.5)

    def hit(self, victim: Warrior):
        super().hit(victim)
        if victim.army:
            if next_warrior := victim.army.next_warrior(victim):
                next_warrior.decrease_health(self.splash)


class Healer(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(health=60, attack=0, *args, **kwargs)
        self.heal_amount = 2

    def heal(self, unit: Warrior):
        unit.increase_health(self.heal_amount)


def fight(unit_1: Warrior, unit_2: Warrior) -> bool:
    attacker, victim = unit_1, unit_2
    while (attacker.is_alive and victim.is_alive):
        attacker.hit(victim)
        victim, attacker = attacker, victim
    return unit_1.is_alive


class Army:
    def __init__(self) -> None:
        self.units = deque()

    def add_units(self, unit_class, count):
        for _ in range(count):
            self.units.append(unit_class(army=self))

    @property
    def is_alive(self) -> bool:
        """Does the army have any units?"""
        return len(self.units) > 0

    @property
    def warrior(self) -> Warrior:
        """Return the first army unit"""
        if self.units:
            return self.units[0]
        else:
            return None

    def pop_warrior(self):
        """Pop unit out of the army list"""
        self.units.popleft()

    def next_warrior(self, unit):
        """Return unit's neighbor unit"""
        try:
            idx = self.units.index(unit)
            return self.units[idx + 1]
        except (ValueError, IndexError) as e:
            return None


class Battle:
    def fight(self, army_1: Army, army_2: Army):
        while army_1.is_alive and army_2.is_alive:
            if fight(army_1.warrior, army_2.warrior):
                army_2.pop_warrior()
            else:
                army_1.pop_warrior()
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
    freelancer = Lancer()
    vampire = Vampire()
    priest = Healer()

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
    assert freelancer.health == 14
    priest.heal(freelancer)
    assert freelancer.health == 16

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True

    army_1 = Army()
    army_1.add_units(Lancer, 1)

    army_2 = Army()
    army_2.add_units(Warrior, 1)
    army_2.add_units(Healer, 1)

    battle = Battle()
    assert battle.fight(army_1, army_2) == False

    print("OK")
