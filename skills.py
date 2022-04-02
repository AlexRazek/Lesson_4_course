class Skill:
    def __init__(self, name: str, damage: float, stamina: float):
        self.name = name
        self.damage = damage
        self.stamina = stamina


class FuryKick(Skill):
    name = "Свирепый пинок"
    stamina = 6
    damage = 12

class PowerShot(Skill):
    name = "Мощный укол"
    stamina = 5
    damage = 15




