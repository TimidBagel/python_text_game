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
    def __init__(self, args) -> None:
        self.healing : int = args["healing"]
        self.rage : int = args["rage"]
        self.stamina : int = args["stamina"]
        self.thorns : int = args["thorns"]


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

# Weapons
weapons = []

goose_beak = ItemWeapon({
    "damage_boost": 0,
    "status_effect": StatusEffect.BLEED,
    "life_steal": 0
    })
toad_hand = ItemWeapon({
    "damage_boost": 1,
    "status_effect": StatusEffect.WEAK,
    "life_steal": 0

})
#This is an important one, all things shoud be 0 or None
no_weapon = ItemWeapon({
    "damage_boost": 0,
    "status_effect": None,
    "life_steal": 0

})

absorbers_wand = ItemWeapon({
    "damage_boost": 0,
    "status_effect": None,
    "life_steal": 45
})

blade_of_agony = ItemWeapon({
    "damage_boost": 5,
    "status_effect": StatusEffect.BLEED,
    "life_steal": 40
})

weapons.append(goose_beak)
weapons.append(toad_hand)
weapons.append(no_weapon)
weapons.append(absorbers_wand)
weapons.append(blade_of_agony)

# Consumables
consumables = []

health_potion = ItemConsumable({
    "healing": 10,
    "rage": 0,
    "stamina": 0,
    "thorns": 0

})

consumables.append(health_potion)