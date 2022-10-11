# Index.py
# Authors: Iain, Jun, Robert, Cormac, Andrew, Drew, Ben
# A Small Text Based Adventure Game

### NOTES ###
# - Classes are defined as Modules. Meaning they are declared in seperate files. Ie `Player.py` and `Entity.py`
#   which are imported using `from ClassName import ClassName`
# - ALWAYS use snake_case when referring to variables and functions
# - ALWAYS Use PascalCase for Objects and Classes
## /NOTES ###
#hibhihiihihihihih
import random
import time
import turtle
import os
import pathlib

### Scripted Modules 
from Entity import Entity, EntityActions
from Item import Item, ItemTypes, ItemWeapon
from InputValidator import input_float, input_int, input_str
from StatusEffect import StatusEffect


### Global Variables
global parent_directory = pathlib.Path(__file__).parent.resolve()
global character_directory = "characters/"
global user_directory = "userdata/"
global user_path = os.path.join(parent_directory, user_directory)
global character_path = os.path.join(user_path, character_directory)

global current_enemy
current_enemy : int = -1

global player_turn # This is used to keep track if the last turn was the players or not
player_turn = True

global enemies
global npcs
enemies = []
npcs = []

#Weapons
goose_beak = ItemWeapon({
    "damage_boost": 0,
    "status_effect": StatusEffect.BLEED

})
toad_hand = ItemWeapon({
    "damage_boost": 1,
    "status_effect": StatusEffect.WEAK

})
no_weapon = ItemWeapon({
    "damage_boost": 0,
    "status_effect": None

    })
crab = Entity({
    "name": "crab",
    "health": 20, 
    "stamina": 10, 
    "strength": 5,
    "poison": 0,
    "skill": 2,
    "actions": [EntityActions.STRIKE.value, EntityActions.ADD_POISON.value],
    "weapon_effect": None,
    "max_stamina": 10,
    "block_amt": 0,
    "Weapon": no_weapon
    
    
})

goose = Entity({
    "name": "goose",
    "health": 30, 
    "stamina": 5, 
    "strength": 8,
    "poison": 0,
    "skill": 1,
    "actions": [EntityActions.STRIKE.value],
    "weapon_effect": StatusEffect.BLEED,
    "max_stamina": 5,
    "block_amt": 0,
    "Weapon": goose_beak
    
})
turtle = Entity({
    "name": "turtle",
    "health": 50, 
    "stamina": 20, 
    "strength": 1,
    "poison": 0,
    "skill": 12,
    "actions": [EntityActions.STRIKE.value, EntityActions.HEAL.value, EntityActions.BLOCK.value],
    "weapon_effect": None,
    "max_stamina": 20,
    "block_amt": 5,
    "Weapon": no_weapon
    
})
toad = Entity({
    "name": "toad",
    "health": 35, 
    "stamina": 30, 
    "strength": 2,
    "poison": 0,
    "skill": 4,
    "actions": [EntityActions.STRIKE.value, EntityActions.ADD_RAGE.value, EntityActions.BLOCK.value],
    "weapon_effect": StatusEffect.WEAK,
    "max_stamina": 30,
    "block_amt": 3,
    "Weapon": no_weapon
    
})
enemies.append(crab)
enemies.append(goose)
#enemies.append(turtle)
enemies.append(toad)
fred = Entity({
    "name": "fred",
    "health": 9001,
    "stamina": 9001,
    "strength": 9001,
    "poison": 9001,
    "skill": 9001,
    "actions": [EntityActions.STRIKE.value, EntityActions.HEAL.value],
    "weapon_effect": None,
    "max_stamina": 9001,
    "block_amt": 0,
    "Weapon": no_weapon
    
})

npcs.append(fred)

player = Entity({
    "name": "player",
    "health": 30, 
    "stamina": 10, 
    "strength": 10,
    "poison": 0,
    "skill": 5,
    "actions": [EntityActions.STRIKE, EntityActions.BLOCK],
    "weapon_effect": None,
    "max_stamina": 10,
    "block_amt": 3,
    "Weapon": no_weapon
     
})
### /Global Variables 


### Input Validation 

### /Input Validation 

def init():
    parent_directory = pathlib.Path(__file__).parent.resolve()

### Inventory 

### /Inventory 



### Action Loop 

### /Action Loop 

### Character Creation
def encrypt(base):
    encrypted = ""
    for x in base:
        cipher = chr(ord(x) + 10)
        if ord(x) >= 97 and ord(x) <= 122:
            if ord(x) > 112:
                cipher = chr(ord(x) - 16)
        elif ord(x) >= 65 and ord(x) <= 90:
            if ord(x) > 80:
                cipher = chr(ord(x) - 16)
        encrypted += cipher
    return encrypted

def decrypt(base):
    decrypted = ""
    for x in base:
        no_cipher = chr(ord(x) - 10)
        if ord(x) >= 97 and ord(x) <= 122:
            if ord(x) < 107:
                no_cipher = chr(ord(x) + 16)
        elif ord(x) >= 65 and ord(x) <= 90:
            if ord(x) < 75:
                no_cipher = chr(ord(x) + 16)
        decrypted += no_cipher
    return decrypted

def new_character():
    if not os.path.exists(user_path):
        os.mkdir(user_path)
    if not os.path.exists(character_path):
        os.mkdir(character_path)

def fetch_character(name):
    return character
### /Character Creation


### Game Loop 
def display_entity_combat_info(entities):
    print()
    for entity in entities:
        time.sleep(0.01)
        print(f"{entity.name.capitalize()}:")
        time.sleep(0.01)
        print(f"| Health: {str(entity.health)}")
        time.sleep(0.01)
        print(f"| Stamina: {str(entity.stamina)}")
        time.sleep(0.01)
        print(f"| Block: {str(entity.block)}")
        
        for s in StatusEffect:
            if entity.status[s] > 0:
                print(f"| {str(s.name)}: {str(entity.status[s])}")
        print("\n")
            
        

def combat():
    input() # press "enter" to continue turns
    time.sleep(0.1)
#   Set enemy if unnassigned

    if enemies == []: return

    global current_enemy
    if current_enemy == -1:
        current_enemy = random.randrange(len(enemies))
        print(f"You encountered a {enemies[current_enemy].name.capitalize()}\n")
        time.sleep(0.1)
        for s in StatusEffect:
            player.status[s] = 0
       

    enemy : Entity = npcs[0]
    #enemy : Entity = enemies[current_enemy]
    
    global player_turn
    if player_turn: # IF its the players turn
        print("|| Player's Turn")
        
#       Poison check
        
        if bool(player.status[StatusEffect.POISON] > 0):
            player.call_status(StatusEffect.POISON, 1)
            print(f"\nYou took 1 damage from poison. You now have {player.health} health remaining and {player.status[StatusEffect.POISON]} turns of poison remaining")
            player.status[StatusEffect.POISON] -= 1
            time.sleep(0.01)
        if player.status[StatusEffect.WEAK] > 0:
            player.status[StatusEffect.WEAK] -= 1
          
            
            time.sleep(0.01)
        #Bleed Check
       

        if player.stamina < player.max_stamina:
            player.stamina += 1
            #We can code in a max stamina stat later as well as a stamina recovery stat you guys don't like to have a ton a variables floating around ~Kit
            #Ive added max stamina ~Kit

        display_entity_combat_info([player, enemy])
        time.sleep(0.01)
        player.block = 0
        print("What will you do?\n")
        time.sleep(0.01)
        print("Player Actions:")
        time.sleep(0.01)
        for action in player.actions:
            print(f"| {action.value}: {action.name.lower().capitalize()}")
            time.sleep(0.01)

    #   Replace with `input_int` when `InputValidation` is made ~Ben
      
        action = input_int("Choose an Action: ")
        print("")

        match action:
            case EntityActions.STRIKE.value:
                if player.stamina > 2:
                    dmg = (player.strength - player.status[StatusEffect.WEAK]) - enemy.block
                    if dmg < 1:
                        dmg = 0
                    enemy.apply_damage(dmg) 
                   
                    print(f"Struck {enemy.name.capitalize()} with {dmg} damage")
                    time.sleep(0.01)
                    print(f"{enemy.name.capitalize()} now has {enemy.health} Health")
                    time.sleep(0.01)
                    if bool(player.status[StatusEffect.BLEED] > 0):
                        print(f"Your rapid movements worsened your bleeding.")
                        time.sleep(0.01)
                        player.call_status(StatusEffect.BLEED, 1)
                        print(f"You took 1 damage from bleeding. You now have {player.health} health remaining")
                        time.sleep(0.01)
                        player.status[StatusEffect.BLEED] += 1
                    player.stamina -= 3
                else:
                    print("You are too tired to take that action!")
                    
                if enemy.is_dead():
                    print(f"\n{enemy.name.capitalize()} has fallen in battle")
                    enemies.remove(enemy)
                    current_enemy = -1
                    
                    for s in StatusEffect:
                        player.status[s] = 0
                    player.stamina = 10
            case EntityActions.BLOCK.value:
                print(f"You added {player.block_amt} block to self!")
                time.sleep(0.01)
                player.block += player.block_amt
                if bool(player.status[StatusEffect.BLEED] > 0):
                    print(f"Your resting lessened your bleeding.")
                    player.status[StatusEffect.BLEED] -= 4
                    if player.status[StatusEffect.BLEED] < 0:
                        player.status[StatusEffect.BLEED] = 0

#       End Player Turn
        if not enemy.is_dead():
            player_turn = False
        
    else: # IF its the enemies turn
        print("|| Enemy Turn")
        if enemy.status[StatusEffect.RAGE]:
            enemy.status[StatusEffect.RAGE] -= 1
        enemy.block = 0
        if enemy.stamina < enemy.max_stamina:
            enemy.stamina += 1
      
        enem_action = random.choice((enemy.actions))
        if enemy.stamina > 2: 
            
            match enem_action:
                case EntityActions.STRIKE.value:
                    dmg = (enemy.strength + enemy.status[StatusEffect.RAGE] + enemy.weapon.damage_boost) - player.block
                    if dmg < 0:
                        dmg = 0
                    player.apply_damage(dmg) 
                      
                    print(f"{enemy.name.capitalize()} hit you for {dmg} damage. You now have {player.health} health left")
                    if enemy.weapon != no_weapon:
                        player.apply_status(enemy.weapon.effect, enemy.skill)
                        print(f"{enemy.name.capitalize()}'s attack added {enemy.skill} {enemy.weapon.effect.name} to you!")
                        
                    enemy.stamina -= 3
                        
                   
                case EntityActions.ADD_POISON.value:
                    # We should make an `add_status` function to `Entity`
                    # I want a bleed status that deals damage when you hit something or use a skill ~Ben
                    #Me Too! I'll do that  ~Kit
                    
                    player.apply_status(StatusEffect.POISON, enemy.skill)
                    print(f"{enemy.name.capitalize()} spit at you and added {enemy.skill} poison!")
                    enemy.stamina -= 2
                        
                case EntityActions.HEAL.value:
                    enemy.apply_damage(-enemy.skill) #Using negative attack damage for healing Big brain ~Kit
                    print(f"{enemy.name.capitalize()} healed for {enemy.skill} damage. It now has {enemy.health} health left")
                    enemy.stamina -= 4
                case EntityActions.BLOCK.value:
                    enemy.block += enemy.block_amt
                    print(f"{enemy.name.capitalize()} added {enemy.block_amt} block to self!")
                case EntityActions.ADD_RAGE.value:
                    enemy.apply_status(StatusEffect.RAGE, enemy.skill)
                    print(f"{enemy.name.capitalize()} is getting pumped and added {enemy.skill} rage to itself!!")
                    enemy.stamina -= 3
            if enemy.stamina < 0:
                enemy.stamina = 0
            
        else:
            print(f"{enemy.name.capitalize()} is too tired to act!")
#       End Enemy Turn
        player_turn = True

    

while enemies != [] and not player.is_dead():
    combat()
if player.is_dead():
    print("You have died!")
### /Game Loop 

input() # end of file pause













#Old Enemy Logic. Saving it here in case I screw up

##       
