from collections import deque


class Warrior:
    def __init__(self, health=50, attack=5, army=None):
        self.MAX_HP: int = health
        self.health: int = health
        self.attack: int = attack
        self.army: Army = army

    @property
    def is_alive(self):
        return self.health > 0

    def calculate_damage(self, damage: int) -> int:
        return damage

    def decrease_health(self, amount: int):
        self.health = max(0, self.health - amount)

    def increase_health(self, amount: int):
        self.health = min(self.MAX_HP, self.health + amount)

    def hit(self, victim):
        damage = victim.calculate_damage(self.attack)
        victim.decrease_health(damage)

        if type(self.next_warrior) is Healer:
            self.next_warrior.heal(self)

        return damage

    @property
    def next_warrior(self):
        if self.army:
            return self.army.next_warrior(self)
        else:
            return None


class Knight(Warrior):
    def __init__(self, attack=7, *args, **kwargs):
        super().__init__(attack=attack, *args, **kwargs)


class Defender(Warrior):
    def __init__(self, health=60, attack=3, defense=2, *args, **kwargs):
        super().__init__(health=health, attack=attack, *args, **kwargs)
        self.defense = defense

    def calculate_damage(self, damage):
        return max(0, damage - self.defense)


class Vampire(Warrior):
    def __init__(self, health=40, attack=4, vampirism=0.5, *args, **kwargs):
        super().__init__(health=health, attack=attack, *args, **kwargs)
        self.vampirism = vampirism

    def hit(self, victim: Warrior):
        damage = super().hit(victim)
        health = int(damage * self.vampirism)
        self.increase_health(health)


class Lancer(Warrior):
    def __init__(self, attack=6, splash=0.5, *args, **kwargs):
        super().__init__(attack=attack, *args, **kwargs)
        self.splash = int(self.attack * splash)

    def hit(self, victim: Warrior):
        super().hit(victim)
        if next_warrior := victim.next_warrior:
            next_warrior.decrease_health(self.splash)


class Healer(Warrior):
    def __init__(self, health=60, attack=0, heal_rate=2, *args, **kwargs):
        super().__init__(health=health, attack=attack, *args, **kwargs)
        self.heal_rate = heal_rate

    def heal(self, unit: Warrior):
        unit.increase_health(self.heal_rate)


def fight(unit_1: Warrior, unit_2: Warrior) -> bool:
    attacker, victim = unit_1, unit_2
    while (attacker.is_alive and victim.is_alive):
        attacker.hit(victim)
        victim, attacker = attacker, victim
    return unit_1.is_alive


class Army:
    def __init__(self) -> None:
        self.units = deque()
        self.duel = False

    def add_units(self, unit, count):
        for _ in range(count):
            self.units.append(unit(army=self))

    @property
    def is_alive(self) -> bool:
        """Does the army have any units?"""
        return self.size > 0

    @property
    def size(self) -> int:
        """Number of live units in army"""
        return len(self.units)

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
        if self.duel:
            return None
        try:
            idx = self.units.index(unit)
            return self.units[idx + 1]
        except (ValueError, IndexError) as e:
            return None

    def pop_dead(self):
        self.units = [unit for unit in self.units if unit.is_alive]


class Battle:
    def fight(self, army_1: Army, army_2: Army) -> bool:
        while army_1.is_alive and army_2.is_alive:
            if fight(army_1.warrior, army_2.warrior):
                army_2.pop_warrior()
            else:
                army_1.pop_warrior()
        return army_1.is_alive

    def straight_fight(self, army_1: Army, army_2: Army) -> bool:
        army_1.duel = True
        army_2.duel = True

        while army_1.is_alive and army_2.is_alive:
            idx, fight_length = 0, min(army_1.size, army_2.size)
            while idx < fight_length:
                attacker, victim = army_1.units[idx], army_2.units[idx]
                if attacker.is_alive:
                    attacker.hit(victim)
                idx += 1

            idx = 0
            while idx < fight_length:
                attacker, victim = army_1.units[idx], army_2.units[idx]
                if victim.is_alive:
                    victim.hit(attacker)
                idx += 1

            army_1.pop_dead()
            army_2.pop_dead()

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

    army_5 = Army()
    army_5.add_units(Warrior, 10)

    army_6 = Army()
    army_6.add_units(Warrior, 6)
    army_6.add_units(Lancer, 5)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    assert battle.straight_fight(army_5, army_6) == False

    army_1 = Army()
    army_2 = Army()

    army_1.add_units(Lancer, 7)
    army_1.add_units(Vampire, 3)
    army_1.add_units(Healer, 1)
    army_1.add_units(Warrior, 4)
    army_1.add_units(Healer, 1)
    army_1.add_units(Defender, 2)

    army_2.add_units(Warrior, 4)
    army_2.add_units(Defender, 4)
    army_2.add_units(Healer, 1)
    army_2.add_units(Vampire, 6)
    army_2.add_units(Lancer, 4)

    battle = Battle()
    assert battle.straight_fight(army_1, army_2) == False

    print("OK")
