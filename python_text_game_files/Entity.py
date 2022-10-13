# Entity.py
# Contributors: Ben, Cormac

from array import array
from enum import Enum
from Item import ItemWeapon
from Item import ItemTypes
from StatusEffect import StatusEffect
import random
from Item import goose_beak, no_weapon, toad_hand, absorbers_wand

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
       
        self.weapon : ItemWeapon = args["Weapon"]#For the equipped weapon (We can bundle this into a dict later) ~Kit
        
        self.status : dict = {}
        for s in StatusEffect:
            self.status[s] = 0

        self.actions : array = args["actions"]
       
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
    def calc_lifesteal(self):
        #Gets the weapon.lifesteal % of the attackers skill. Its really cool! :D ~Kit
        one_percent = self.skill / 100
        amount_steal = one_percent * self.weapon.life_steal
        amount_steal = round(amount_steal)
        return amount_steal
    
      
class EntityActions(Enum): 
    STRIKE = 0
    BLOCK = 1
    ESCAPE = 2
    ADD_POISON = 3
    HEAL = 4
    ADD_WEAK = 5
    ADD_RAGE = 6

#Enemies

crab = Entity({
    "name": "crab",
    "health": 20, 
    "stamina": 10, 
    "strength": 5,
    #"poison": 0,
    "skill": 2,
    "actions": [EntityActions.STRIKE.value, EntityActions.ADD_POISON.value],
    
    "max_stamina": 10,
    "block_amt": 0,
    "Weapon": no_weapon
    
    
})

goose = Entity({
    "name": "goose",
    "health": 30, 
    "stamina": 5, 
    "strength": 8,
    #"poison": 0,
    "skill": 1,
    "actions": [EntityActions.STRIKE.value],
    
    "max_stamina": 5,
    "block_amt": 0,
    "Weapon": goose_beak
    
})
turtle = Entity({
    "name": "turtle",
    "health": 25, 
    "stamina": 40, 
    "strength": 1,
    #"poison": 0,
    "skill": 12,
    "actions": [EntityActions.STRIKE.value, EntityActions.HEAL.value, EntityActions.BLOCK.value],
    
    "max_stamina": 20,
    "block_amt": 4,
    "Weapon": no_weapon
    
})
toad = Entity({
    "name": "toad",
    "health": 35, 
    "stamina": 30, 
    "strength": 2,
    #"poison": 0,
    "skill": 4,
    "actions": [EntityActions.STRIKE.value, EntityActions.ADD_RAGE.value, EntityActions.BLOCK.value],
   
    "max_stamina": 30,
    "block_amt": 3,
    "Weapon": toad_hand
    
})
rabbit = Entity({
    "name": "rabbit",
    "health": 16,
    "stamina": 30,
    "strength": 11,
    "poison": 0,
    "skill": 6,
    "actions": [EntityActions.STRIKE.value, EntityActions.HEAL.value],
    
    "max_stamina": 30,
    "block_amt": 0,
    "Weapon": no_weapon
})
#Lets start moving away from the animals they are really cool but we should make them cooler
dark_sprite = Entity({
    "name": "Dark Sprite",
    "health": 25, 
    "stamina": 15, 
    "strength": 3,
    #"poison": 0,
    "skill": 6,
    "actions": [EntityActions.STRIKE.value, EntityActions.ADD_POISON.value, EntityActions.BLOCK.value, EntityActions.HEAL.value],
   
    "max_stamina": 15,
    "block_amt": 4,
    
    "Weapon": absorbers_wand
    })



