from __future__ import annotations
from abc import ABC, abstractmethod
from equipment import Equipment, Weapon, Armor
from classes import UnitClass
from random import randint
from typing import Optional


# from skills import Skill, FuryKick, PowerShot

#
# class Unit(ABC):
#     name: str = ...
#     max_health: float = ...
#     max_stamina: float = ...
#     attack: float = ...
#     stamina: float = ...
#     armor: float = ...
#     skill: Skill = ...
#
# class Warrior(Unit):
#     name: 'Воин'
#     max_health: 60.0
#     max_stamina: 30.0
#     attack: 0.8
#     stamina: 0.9
#     armor: 1.2
#     skill: FuryKick
#
#
# class Burglar(Unit):
#     name: 'Вор'
#     max_health: 50.0
#     max_stamina: 25.0
#     attack: 1.5
#     stamina: 1.2
#     armor: 1.0
#     skill: PowerShot

class BaseUnit(ABC):

    def __init__(self, name: str, unit_class: UnitClass):
        self.name = name
        self.unit_class = unit_class
        self.hp = self.unit_class.max_health
        self.stamina = self.unit_class.max_stamina
        self.weapon = Equipment().get_weapon('')
        self.armor = Equipment().get_armor('')
        self._is_skill_used: bool = False

    @property
    def health_points(self):
        return round(self.hp, 1)

    @health_points.setter
    def health_points(self, value):
        self.hp = value

    @property
    def stamina_points(self):
        return round(self.stamina, 1)

    @stamina_points.setter
    def stamina_points(self, value):
        self.stamina = value

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor):
        self.armor = armor
        return f"{self.name} экипирован броней {self.weapon.name}"

    def _count_damage(self, target: BaseUnit) -> int:
        self.stamina -= self.weapon.stamina_per_hit * self.unit_class.stamina
        damage = self.weapon.damage * self.unit_class.attack
        if target.stamina > target.armor.stamina_per_turn * target.unit_class.stamina:
            target.stamina -= target.armor.stamina_per_turn * target.unit_class.stamina
            damage = damage - target.armor.defence * target.unit_class.armor
        else:
            pass
        damage = target.get_damage(damage)
        return damage

    def get_damage(self, damage: int) -> Optional[int]:
        if damage > 0:
            self.hp -= damage
            self.hp = self.hp
            return round(damage, 1)
        return None

    @abstractmethod
    def hit(self, target: BaseUnit) -> str:
        pass

    def use_skill(self, target: BaseUnit) -> str:
        if self._is_skill_used:
            return "Навык уже использован"
        self._is_skill_used = True
        return self.unit_class.skill.use(user=self, target=target)


class EnemyUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        if randint(0, 100) < 10 and self.stamina >= self.unit_class.skill.stamina and not self._is_skill_used:
            return self.use_skill(target)
        if self.stamina >= self.weapon.stamina_per_hit * self.unit_class.stamina:
            damage = self._count_damage(target)
            if damage:
                return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} и наносит Вам {damage} урона."
            return f"{self.name} используя {self.weapon.name} наносит удар, но Ваш(а) {target.armor.name} его останавливает."
        return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."


class PlayerUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        if self.stamina >= self.weapon.stamina_per_hit * self.unit_class.stamina:
            damage = self._count_damage(target)
            if damage:
                return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} соперника и наносит {damage} урона."
            return f"{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name} cоперника его останавливает."
        return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."
