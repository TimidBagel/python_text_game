# Entity.py
# Contributors: Ben, Cormac

from array import array
from enum import Enum
from Item import ItemTypes
from StatusEffect import StatusEffect
import random

class Entity:
    def __init__(self, args) -> None:
        self.name = args["name"]
        self.health : int = args["health"]
        self.stamina : int = args["stamina"]
        self.strength : int = args["strength"]
        
        self.skill : int = args["skill"] #Skill will be used for special attacks and the like ~Kit
        self.inventory : dict = {
            ItemTypes.WEAPON: [],
            ItemTypes.ACCESSORY: [],
            ItemTypes.CONSUMABLE: []
        }
        self.status : dict = {}
        for s in StatusEffect:
            self.status[s] = 0

        self.actions : array = args["actions"]
        self.weapon_effect : StatusEffect = args["weapon_effect"]
        self.block_amt : int = args["block_amt"]
        self.block : int = 0
        self.max_stamina : int = args["max_stamina"]
        

#   Sets `health` to 0 if its below 0
    def apply_damage(self, amt: int) -> None:
        self.health = int((self.health - amt) > 0) * abs(self.health - amt)

    def apply_status(self, status: StatusEffect, amt: int) -> None:
            self.status[status] += amt
        

    def call_status(self, status: StatusEffect, amt: int):
        match status:
            case StatusEffect.POISON:
                self.apply_damage(amt)
            case StatusEffect.BLEED:
                self.apply_damage(amt)

    def is_dead(self) -> bool:
        return self.health <= 0
       #WE will eventually add a get_modifer def that can get all the modifiers for an attack.
class EntityActions(Enum): #We need some way to remove actions for enemies form the player action list (And i dont think ben would be happy if I made a new Enum) ~Kit
    STRIKE = 0
    BLOCK = 1
    ESCAPE = 2
    ADD_POISON = 3
    HEAL = 4
    ADD_WEAK = 5
    ADD_RAGE = 6
    #On second thought, is it possible to have an enum with a parameter? we could have ADDSTATUS(), and that could work for multiple maybe.

#       End Enemy Turn
       


# We need different actions for the statuses bunching them all up into one has several issues. A. This means an enemy couldn't do more than one status (Limits enemy dynamism) B. We need different action text for each of them. you can't spit at someone and make them bleed. ~Kit
#Ok Teeeeeechnically i found a way for it to work with one thing (See the StatusEffect script as well as some of the combat script) But I still think having one for each is better as it allows for more unique enemies and we should avoid having a ton of lists lying aroun ~Kit

#I think this could be a cool feature to add. Each weapon you get has unique skills ~Ben

#   Good idea, this could also be used for an enemy unique skill ~Kit
#   Scratch that, Im working on enemy AI to be even cooler :D ~Kit

#   SKILL = 3


