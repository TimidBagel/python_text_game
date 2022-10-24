# Entity.py
# Contributors: Ben, Cormac
#Testing
from array import array
from enum import Enum
from Item import ItemWeapon
from Item import ItemTypes
from Item import ItemConsumable
from StatusEffect import StatusEffect
from Race import monster
from Class import peasant
import random
from Item import goose_beak, no_weapon, toad_hand, absorbers_wand, blade_of_agony



class Entity:
    def __init__(self, args) -> None:
        self.name = args["name"]
        self.race = args.get('race', monster)
        self.Class = args.get('Class', peasant)
        self.health : int = args["health"]
        self.max_hp : int = args["max_hp"]
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

        self.raw : dict = args
        self.is_enemy : bool = args["is_enemy"]
        

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
    def take_turn(self, target, action: int):
        if self.stamina > 2: 
            
            match action:

                
                case EntityActions.STRIKE.value:
                    dmg = (self.strength + (self.status[StatusEffect.RAGE] - self.status[StatusEffect.WEAK]) + self.weapon.damage_boost) - target.block
                    if dmg < 0:
                        dmg = 0
                    target.apply_damage(dmg) 
                    
                    print(f"{self.name.capitalize()} hit {target.name.capitalize()} for {dmg} damage. {target.name.capitalize()} now has {target.health} health left")
                    if self.weapon != no_weapon:
                        if self.weapon.effect != None:
                            target.apply_status(self.weapon.effect, self.skill)
                            print(f"{self.name.capitalize()}'s attack added {self.skill} {self.weapon.effect.name} to {target.name.capitalize()}!")
                        if self.weapon.life_steal > 0:
                            self.apply_damage(-self.calc_lifesteal())
                            print(f"{self.name.capitalize()}'s attack drained {self.calc_lifesteal()} health from {target.name.capitalize()}!")
                    if target.status[StatusEffect.THORNS] > 0:
                        self.apply_damage(target.status[StatusEffect.THORNS])
                        print(f"{target.name.capitalize()}'s thorns hurt {self.name.capitalize()} for {target.status[StatusEffect.THORNS]}. They now have {target.health} health left")
                        target.status[StatusEffect.THORNS] -= dmg
                        if target.status[StatusEffect.THORNS] < 0:
                            target.status[StatusEffect.THORNS] = 0
                        
                        
                    self.stamina -= 3
                        


                   
             
                        
                case EntityActions.HEAL.value:
                    self.apply_damage(-self.skill) #Using negative attack damage for healing Big brain ~Kit
                    print(f"{self.name.capitalize()} healed for {self.skill} damage. It now has {self.health} health left")
                    self.stamina -= 4

                    
                case EntityActions.BLOCK.value:
                    self.block += self.block_amt
                    print(f"{self.name.capitalize()} added {self.block_amt} block to self!")

                    
                case EntityActions.ADD_RAGE.value:
                    self.apply_status(StatusEffect.RAGE, self.skill)
                    print(f"{self.name.capitalize()} is getting pumped and added {self.skill} rage to itself!!")
                    self.stamina -= 3
                    
                case EntityActions.ADD_POISON.value:
                    # We should make an `add_status` function to `Entity`
                    # I want a bleed status that deals damage when you hit something or use a skill ~Ben
                    #Me Too! I'll do that  ~Kit
                    
                    target.apply_status(StatusEffect.POISON, self.skill)
                    print(f"{self.name.capitalize()} spit at {target.name.capitalize()} and added {self.skill} poison!")
                    self.stamina -= 2
                case EntityActions.ADD_THORNS.value:
                    self.apply_status(StatusEffect.THORNS, self.skill)
                    self.stamina -= 2
                    print(f"{self.name.capitalize()} braced and added {self.skill} thorns to itself!!")
                    
        else:
            print(f"{self.name.capitalize()} is too tired to act!")
       
            
    
      
class EntityActions(Enum): 
    STRIKE = 0
    BLOCK = 1
    ESCAPE = 2
    ADD_POISON = 3
    HEAL = 4
    ADD_WEAK = 5
    ADD_RAGE = 6
    ADD_THORNS = 7
    USE_ITEM = 8

#Enemies
enemies = []

crab = Entity({
    "name": "crab",
    "health": 20,
    "max_hp": 20, 
    "stamina": 10, 
    "strength": 5,
    "poison": 0,
    "skill": 2,
    "actions": [EntityActions.STRIKE.value, EntityActions.ADD_POISON.value],
    "max_stamina": 10,
    "block_amt": 0,
    "Weapon": no_weapon,
    "is_enemy": True  
})

goose = Entity({
    "name": "goose",
    "health": 30, 
    "max_hp": 30,
    "stamina": 5, 
    "strength": 8,
    "poison": 0,
    "skill": 1,
    "actions": [EntityActions.STRIKE.value],
    
    "max_stamina": 5,
    "block_amt": 0,
    "Weapon": goose_beak,
    "is_enemy": True
    
})
turtle = Entity({
    "name": "turtle",
    "health": 30, 
    "max_hp": 45,
    "stamina": 20, 
    "strength": 1,
    "poison": 0,
    "skill": 12,
    "actions": [EntityActions.STRIKE.value, EntityActions.HEAL.value, EntityActions.BLOCK.value],
    "max_stamina": 20,
    "block_amt": 5,
    "Weapon": no_weapon,
    "is_enemy": True
    
})
toad = Entity({
    "name": "toad",
    "health": 35, 
    "max_hp": 35,
    "stamina": 30, 
    "strength": 2,
    "poison": 0,
    "skill": 4,
    "actions": [EntityActions.STRIKE.value, EntityActions.ADD_RAGE.value, EntityActions.BLOCK.value],
    "max_stamina": 30,
    "block_amt": 3,
    "Weapon": toad_hand,
    "is_enemy": True
    
})
rabbit = Entity({
    "name": "rabbit",
    "health": 16,
    "max_hp": 16,
    "stamina": 30,
    "strength": 11,
    "poison": 0,
    "skill": 6,
    "actions": [EntityActions.STRIKE.value, EntityActions.HEAL.value],
    "max_stamina": 30,
    "block_amt": 0,
    "Weapon": no_weapon,
    "is_enemy": True
})
#Lets start moving away from the animals they are really cool but we should make them cooler
dark_sprite = Entity({
    "name": "Dark Sprite",
    "health": 25, 
    "max_hp": 25,
    "stamina": 15, 
    "strength": 3,
    "poison": 0,
    "skill": 6,
    "actions": [EntityActions.STRIKE.value, EntityActions.ADD_POISON.value, EntityActions.BLOCK.value, EntityActions.HEAL.value],
    "max_stamina": 15,
    "block_amt": 4,
    "Weapon": absorbers_wand,
    "is_enemy": True
    })
steelblade_squire = Entity({
    "name": "Steelblade Squire",
    "health": 45, 
    "max_hp": 45,
    "stamina": 25, 
    "strength": 6,
    "poison": 0,
    "skill": 8,
    "actions": [EntityActions.STRIKE.value, EntityActions.BLOCK.value, EntityActions.ADD_THORNS.value],
    "max_stamina": 25,
    "block_amt": 4,
    "Weapon": no_weapon,
    "is_enemy": True
})

enemies.append(goose)
enemies.append(turtle)
enemies.append(toad)
enemies.append(rabbit)
enemies.append(dark_sprite)
enemies.append(steelblade_squire)

# NPCs
npcs = []

fred = Entity({
    "name": "fred",
    "health": 9001,
    "max_hp": 9001,
    "stamina": 9001,
    "strength": 9001,
    "poison": 9001,
    "skill": 9001,
    "actions": [EntityActions.STRIKE.value, EntityActions.HEAL.value],
    "max_stamina": 9001,
    "block_amt": 0,
    "Weapon": no_weapon,
    "is_enemy": True
    
})
martyr = Entity({ #martyr npc 
    "name": "martyr",
    "health": 90,
    "max_hp": 90,
    "stamina": 20,
    "strength": 3,
    "poison": 4,
    "skill": 10,
    "actions": [EntityActions.STRIKE.value, EntityActions.BLOCK.value, EntityActions.ADD_RAGE],
    "max_stamina": 20,
    "block_amt": 1,
    "Weapon": blade_of_agony,
    "is_enemy": True
})

npcs.append(fred)
npcs.append(martyr)