from dataclasses import dataclass
from skills import Skill, PowerShot, FuryKick


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name="Воин",
    max_health=60.0,
    max_stamina=30.0,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=FuryKick()
)

BurglarClass = UnitClass(
    name="Вор",
    max_health=50.0,
    max_stamina=25.0,
    stamina=1.2,
    attack=1.5,
    armor=1.0,
    skill=PowerShot()
)

unit_classes = {
    WarriorClass.name: WarriorClass,
    BurglarClass.name: BurglarClass,
}

# name: str
# max_health: float
# max_stamina: float
# attack: float
# stamina: float
# armor: float
# skill: ConcreteSkill