# Item.py
# Contributors: Ben

from enum import Enum
from tokenize import String

class Item:
    def __init__(self) -> None:
        name : String
        item_type : ItemTypes


class ItemWeapon(Item):
    def __init__(self) -> None:
        damage : int

class ItemAccessory(Item):
    def __init__(self) -> None:
#       Someone else can decide what goes here. Not sure how the system works yet ~Ben
        pass

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