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
        self.poison : int = args["poison"]
        self.skill : int = args["skill"] #Skill will be used for special attacks and the like ~Kit
        self.inventory : dict = {
            ItemTypes.WEAPON: [],
            ItemTypes.ACCESSORY: [],
            ItemTypes.CONSUMABLE: []
        }
        self.ai : [] = args["ai"] #This controls which actions the entity can do (useless for player, leave blank for their spawn call)
        #Someone can figure out a better alternitive for this just dont erase all my work mmk ~Kit
        

#   Sets `health` to 0 if its below 0
    def apply_damage(self, amt: int) -> None:
        self.health = int((self.health - amt) > 0) * abs(self.health - amt)

    def is_dead(self) -> bool:
        return self.health <= 0

class EntityActions(Enum): #We need some way to remove actions for enemies form the player action list (And i dont think ben would be happy if I made a new Enum) ~Kit
    STRIKE = 0
    BLOCK = 1
    ESCAPE = 2
    ADDPOISON = 3
#   I think this could be a cool feature to add. Each weapon you get has unique skills ~Ben
#   Good idea, this could also be used for an enemy unique skill ~Kit
#   Scratch that, Im working on enemy AI to be even cooler :D ~Kit

#   SKILL = 3



