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
    def __init__(self, health=30, attack=3, heal_power=3):
        super().__init__(health=health, attack=attack, heal_power=heal_power)


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

    def decrease_health(self, amount: int):
        self.health = max(0, self.health - amount)

    def increase_health(self, amount: int):
        self.health = min(self.max_health, self.health + amount)

    def hit(self, victim):
        damage = victim.calculate_damage(self.attack)
        victim.decrease_health(damage)

        if type(self.next_warrior) is Healer:
            self.next_warrior.heal(self)

        return damage

    def equip_weapon(self, weapon: Weapon):
        self.weapons.append(weapon)
        for key, val in vars(weapon).items():
            if key not in vars(self):
                continue
            if key == 'health':
                self.max_health = max(0, self.max_health + val)
                self.health = max(0, min(self.max_health, self.health + val))
            elif key == 'attack':
                self.attack = max(0, self.attack + val)
            elif key == 'defence':
                self.defence = max(0, self.defence + val)
            elif key == 'vampirism':
                self.vampirism = max(0, self.vampirism + val)
            elif key == 'heal_power':
                self.heal_power = max(0, self.heal_power + val)


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
        self.increase_health(health)


class Lancer(Warrior):
    def __init__(self, attack=6, splash=50, *args, **kwargs):
        super().__init__(attack=attack, *args, **kwargs)
        self.splash = splash

    def hit(self, victim: Warrior):
        super().hit(victim)
        if next_warrior := victim.next_warrior:
            damage = (self.attack * self.splash) // 100
            next_warrior.decrease_health(damage)


class Healer(Warrior):
    def __init__(self, health=60, attack=0, heal_power=2, *args, **kwargs):
        super().__init__(health=health, attack=attack, *args, **kwargs)
        self.heal_power = heal_power

    def heal(self, unit: Warrior):
        unit.increase_health(self.heal_power)


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

    # fight tests
    ogre = Warrior()
    lancelot = Knight()
    richard = Defender()
    eric = Vampire()
    freelancer = Lancer()
    priest = Healer()

    sword = Sword()
    shield = Shield()
    axe = GreatAxe()
    katana = Katana()
    wand = MagicWand()
    super_weapon = Weapon(50, 10, 5, 150, 8)

    ogre.equip_weapon(sword)
    ogre.equip_weapon(shield)
    ogre.equip_weapon(super_weapon)
    lancelot.equip_weapon(super_weapon)
    richard.equip_weapon(shield)
    eric.equip_weapon(super_weapon)
    freelancer.equip_weapon(axe)
    freelancer.equip_weapon(katana)
    priest.equip_weapon(wand)
    priest.equip_weapon(shield)

    ogre.health == 125
    lancelot.attack == 17
    richard.defense == 4
    eric.vampirism == 200
    freelancer.health == 15
    priest.heal_power == 5

    fight(ogre, eric) == False
    fight(priest, richard) == False
    fight(lancelot, freelancer) == True

    my_army = Army()
    my_army.add_units(Knight, 1)
    my_army.add_units(Lancer, 1)

    enemy_army = Army()
    enemy_army.add_units(Vampire, 1)
    enemy_army.add_units(Healer, 1)

    my_army.units[0].equip_weapon(axe)
    my_army.units[1].equip_weapon(super_weapon)

    enemy_army.units[0].equip_weapon(katana)
    enemy_army.units[1].equip_weapon(wand)

    battle = Battle()

    battle.fight(my_army, enemy_army) == True

    print("OK")
