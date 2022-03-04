from collections import deque


class Weapon():
    def __init__(self, health=0, attack=0, defense=0, vampirism=0, heal_power=0):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.heal_power = heal_power


class Sword(Weapon):
    def __init__(self, health=5, attack=2):
        super().__init__(health=health, attack=attack)


class Shield(Weapon):
    def __init__(self, health=20, attack=-1, defense=2):
        super().__init__(health=health, attack=attack, defense=defense)


class GreatAxe(Weapon):
    def __init__(self, health=-15, attack=5, defense=-2, vampirism=10):
        super().__init__(health=health, attack=attack, defense=defense, vampirism=vampirism)


class Katana(Weapon):
    def __init__(self, health=-20, attack=6, defense=-5, vampirism=50):
        super().__init__(health=health, attack=attack, defense=defense, vampirism=vampirism)


class MagicWand(Weapon):
    def __init__(self, health=30, attack=3, heal_power=3):
        super().__init__(health=health, attack=attack, heal_power=heal_power)


class Warrior:
    def __init__(self, health=50, attack=5, army=None, weapons=[]):
        self.max_health: int = health
        self.health: int = health
        self.attack: int = attack
        self.army: Army = army
        self.weapons = weapons

    @property
    def is_alive(self):
        return self.health > 0

    @property
    def next_warrior(self):
        if self.army:
            return self.army.next_warrior(self)
        else:
            return None

    def calculate_damage(self, damage: int) -> int:
        return damage

    def update_health(self, health, max_health=None):
        if max_health:
            self.max_health = max(0, self.max_health + max_health)
        self.health = max(0, min(self.max_health, self.health + health))

    def hit(self, victim):
        damage = victim.calculate_damage(self.attack)
        victim.update_health(-damage)

        if type(self.next_warrior) is Healer:
            self.next_warrior.heal(self)

        return damage

    def equip_weapon(self, weapon: Weapon):
        self.weapons.append(weapon)
        for key, val in vars(weapon).items():
            if key not in vars(self):
                continue
            if key == 'health':
                self.update_health(health=val, max_health=val)
            else:
                cur_val = getattr(self, key)
                new_val = max(0, cur_val + val)
                setattr(self, key, new_val)


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
    def __init__(self, health=40, attack=4, vampirism=50, *args, **kwargs):
        super().__init__(health=health, attack=attack, *args, **kwargs)
        self.vampirism = vampirism

    def hit(self, victim: Warrior):
        damage = super().hit(victim)
        health = (damage * self.vampirism) // 100
        self.update_health(health)


class Lancer(Warrior):
    def __init__(self, attack=6, splash=50, *args, **kwargs):
        super().__init__(attack=attack, *args, **kwargs)
        self.splash = splash

    def hit(self, victim: Warrior):
        super().hit(victim)
        if next_warrior := victim.next_warrior:
            damage = (self.attack * self.splash) // 100
            next_warrior.update_health(-damage)


class Healer(Warrior):
    def __init__(self, health=60, attack=0, heal_power=2, *args, **kwargs):
        super().__init__(health=health, attack=attack, *args, **kwargs)
        self.heal_power = heal_power

    def heal(self, unit: Warrior):
        unit.update_health(self.heal_power)


class Warlord(Defender):
    def __init__(self, health=100, attack=4, *args, **kwargs):
        super().__init__(health=health, attack=attack, *args, **kwargs)


class Army:
    def __init__(self) -> None:
        self.units = deque()
        self.duel = False
        self.has_warlord = False

    def add_units(self, unit, count):
        if unit is Warlord:
            if not self.has_warlord:
                self.units.append(unit(army=self))
                self.has_warlord = True
        else:
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

    def move_units(self):
        if not self.has_warlord:
            return

        lancers = []
        healers = []
        warlord = []
        others = []

        for unit in self.units:
            if type(unit) is Lancer:
                lancers.append(unit)
            elif type(unit) is Healer:
                healers.append(unit)
            elif type(unit) is Warlord:
                warlord.append(unit)
            else:
                others.append(unit)

        if lancers:
            sorted_units = lancers[:1] + healers + lancers[1:] + others + warlord
        else:
            sorted_units = others[:1] + healers + others[1:] + warlord

        self.units = deque(sorted_units)


class Battle:
    def fight(self, army_1: Army, army_2: Army) -> bool:
        army_1.move_units()
        army_2.move_units()
        while army_1.is_alive and army_2.is_alive:
            if fight(army_1.warrior, army_2.warrior):
                army_2.pop_warrior()
                army_2.move_units()
            else:
                army_1.pop_warrior()
                army_1.move_units()
        return army_1.is_alive

    def straight_fight(self, army_1: Army, army_2: Army) -> bool:
        army_1.duel = True
        army_2.duel = True
        while army_1.is_alive and army_2.is_alive:
            for attacker, victim in zip(army_1.units, army_2.units):
                fight(attacker, victim)
            army_1.pop_dead()
            army_2.pop_dead()

        return army_1.is_alive


def fight(unit_1: Warrior, unit_2: Warrior) -> bool:
    attacker, victim = unit_1, unit_2
    while (attacker.is_alive and victim.is_alive):
        attacker.hit(victim)
        victim, attacker = attacker, victim
    return unit_1.is_alive


if __name__ == '__main__':

    ronald = Warlord()
    heimdall = Knight()

    fight(heimdall, ronald) == False

    my_army = Army()
    my_army.add_units(Warlord, 1)
    my_army.add_units(Warrior, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 2)

    enemy_army = Army()
    enemy_army.add_units(Warlord, 3)
    enemy_army.add_units(Vampire, 1)
    enemy_army.add_units(Healer, 2)
    enemy_army.add_units(Knight, 2)

    my_army.move_units()
    enemy_army.move_units()

    type(my_army.units[0]) == Lancer
    type(my_army.units[1]) == Healer
    type(my_army.units[-1]) == Warlord

    type(enemy_army.units[0]) == Vampire
    type(enemy_army.units[-1]) == Warlord
    type(enemy_army.units[-2]) == Knight

    # 6, not 8, because only 1 Warlord per army could be
    len(enemy_army.units) == 6

    battle = Battle()

    battle.fight(my_army, enemy_army) == True

    # 24. Battle/0
    army_1 = Army()
    army_2 = Army()

    army_1.add_units(Warrior, 2)
    army_1.add_units(Lancer, 2)
    army_1.add_units(Defender, 1)
    army_1.add_units(Warlord, 3)

    army_2.add_units(Warlord, 2)
    army_2.add_units(Vampire, 1)
    army_2.add_units(Healer, 5)
    army_2.add_units(Knight, 2)

    army_1.move_units()
    army_2.move_units()

    battle = Battle()
    assert battle.fight(army_1, army_2) == False

    print("OK")
