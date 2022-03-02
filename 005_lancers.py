from collections import deque


class Warrior:
    def __init__(self, health=50, attack=5, army=None):
        self.health = health
        self.attack = attack
        self.army = army

    @property
    def is_alive(self):
        return self.health > 0

    def calculate_damage(self, damage: int) -> int:
        return damage

    def decrease_health(self, damage: int):
        self.health -= self.calculate_damage(damage)

    def hit(self, victim):
        victim.decrease_health(self.attack)

    def next(self):
        if not self.army:
            return None

        try:
            idx = self.army.units.index(self)
            return self.army.units[idx + 1]
        except (ValueError, IndexError) as e:
            return None


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
        super().hit(victim)
        self.health += int(victim.calculate_damage(self.attack) * self.vampirism)


class Lancer(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(attack=6, *args, **kwargs)
        self.splash = int(self.attack * 0.5)

    def hit(self, victim: Warrior):
        super().hit(victim)
        next = victim.next()
        if next:
            self.hit_with_splash(next)

    def hit_with_splash(self, victim: Warrior):
        victim.decrease_health(self.splash)


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
