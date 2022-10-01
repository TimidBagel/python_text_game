# Entity.py
# Contributors: Ben, Cormac

from enum import Enum
from Item import ItemTypes


class Entity:
    def __init__(self, args) -> None:
        self.name = args["name"]
        self.health : int = args["health"]
        self.stamina : int = args["stamina"]
        self.strength : int = args["strength"]
        self.inventory : dict = {
            ItemTypes.WEAPON: [],
            ItemTypes.ACCESSORY: [],
            ItemTypes.CONSUMABLE: []
        }

#   Sets `health` to 0 if its below 0
    def apply_damage(self, amt: int) -> None:
        self.health = int((self.health - amt) > 0) * abs(self.health - amt)

    def is_dead(self) -> bool:
        return self.health <= 0

class EntityActions(Enum):
    STRIKE = 0
    BLOCK = 1
    ESCAPE = 2
#   I think this could be a cool feature to add. Each weapon you get has unique skills ~Ben
#   SKILL = 3
