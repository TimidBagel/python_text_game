# Item.py
# Contributors: Ben

from enum import Enum
from tokenize import String
    
from StatusEffect import StatusEffect
class Item:
    def __init__(self) -> None:
        name : String
        item_type : ItemTypes


class ItemWeapon(Item):
    def __init__(self, args) -> None:
        self.damage_boost : int = args["damage_boost"]
        self.effect : StatusEffect = args["status_effect"]
        self.life_steal : int = args["life_steal"]
        

class ItemAccessory(Item):
    def __init__(self) -> None:
        effect : EffectTypes
        target : EffectTarget
        

class ItemConsumable(Item):
    def __init__(self, effect, intensity) -> None:
        self.effect : ConsumableTypes = effect
        self.intensity : int = intensity


class ItemTypes(Enum):
    WEAPON = 0
    ACCESSORY = 1
    CONSUMABLE = 2

class ConsumableTypes(Enum):
    HEALTH = 0
    DAMAGE = 1
    DEFENSE = 2
class EffectTypes(Enum):
    #We will definitly add more stuff here ~Kit
    POISON = 1
    WEAKNESS = 2
    STRENGTH = 3
    
    NOTHING = 0

class EffectTarget(Enum):
    WEAPON = 0
    SELF = 1
    ENEMY = 2
