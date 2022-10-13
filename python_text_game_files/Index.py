# Index.py
# Authors: Iain, Jun, Robert, Cormac, Andrew, Drew, Ben, Patrick
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
from Debug import Console
#Alternatively, we can import all the weapons from ITEM ~Kit
from Item import goose_beak, no_weapon, toad_hand, absorbers_wand, blade_of_agony
#I will do the same with enemies
from Entity import crab, turtle, toad, goose, rabbit, dark_sprite

### Global Variables
global parent_directory
global character_directory
global user_directory
global user_path
global character_path

global current_enemy
current_enemy : int = -1

global enemy_encounter_grp
enemy_encounter_grp : int = 1

global enc_counter
enc_counter = random.randint(1, 3)

global npc_encounters
npc_encounters : int = 1

global player_turn # This is used to keep track if the last turn was the players or not
player_turn = True

global enemies
global npcs
enemies = []
npcs = []

#Weapons



#Enemies

enemies.append(crab)
enemies.append(goose)
enemies.append(turtle)
enemies.append(toad)
enemies.append(rabbit)
enemies.append(dark_sprite)
#NPCs
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
    "Weapon": no_weapon
    
})
draughlix = Entity({ #martyr npc 
    "name": "draughlix",
    "health": 90,
    "max_hp": 90,
    "stamina": 20,
    "strength": 3,
    "poison": 4,
    "skill": 10,
    "actions": [EntityActions.STRIKE.value, EntityActions.BLOCK.value, EntityActions.ADD_RAGE],
    "max_stamina": 20,
    "block_amt": 1,
    "Weapon": blade_of_agony
})
npcs.append(fred)
npcs.append(draughlix)

player = Entity({
    "name": "player",
    "health": 30, 
    "max_hp": 30,
    "stamina": 15, 
    "strength": 15,
    "poison": 0,
    "skill": 5,
    "actions": [EntityActions.STRIKE, EntityActions.BLOCK],
    "max_stamina": 15,
    "block_amt": 3,
    "Weapon": no_weapon
     
})
### /Global Variables 


### Input Validation 

### /Input Validation 

def init():
    parent_directory = pathlib.Path(__file__).parent.resolve()
    character_directory = "characters/"
    user_directory = "userdata/"
    user_path = os.path.join(parent_directory, user_directory)
    character_path = os.path.join(user_path, character_directory)

### Inventory 

### /Inventory 

### Action Loop 
def progression(): #progression loop wip -p
    global enemy_encounter_grp
    global npc_encounters
    global npcs
    global current_npc
    global enemies
    global combat
    if enemy_encounter_grp == 0:
        input()
        global enc_counter
        enc_counter = random.randint(1, 2)
        print(f"after fighting through the seemingly endless amounts of animals you have come across...")
        if enc_counter == 1:
            print("another enemy!")

            enemy_encounter_grp += 1
            combat()
        if enc_counter == 2:
            npc_encounters = random.randint(0, len(npcs)-1)
            if npc_encounters == 0:
                print("You have found fred. Oh no. He rises into the air, and snaps your neck, killing you instantly :D")
            if npc_encounters == 1: #We can change to a match/case later

                current_npc = npcs[1]
                print(f"you have come across the {current_npc.name.capitalize()}") 

                has_chosen = False
                valid_m_actions = ['1','2','3']
                draughlix_fight = False
                while has_chosen == False:
                    m_choice = input(f"""The Draughlix has offered you a deal you can gain more power in exchange for your life force... \n
                    do you 
                    1) accept -10 health for +5 damage
                    2) decline (move on)
                    3) fight the Draughlix\n""")
                    if m_choice in valid_m_actions:
                        has_chosen = True
                    else:
                        has_chosen = False
                if m_choice == '1':
                    player.max_hp -= 10
                    player.health = player.max_hp
                    if player.max_hp < 1:
                        print("Draughlix: You imbecile why would you sacrifice health you didn't have? Now you are going to die.")
                    else:
                        print("Draughlix: The dark pact is sealed. Your strength has been increased by 5... continue on mortal.")
                        player.strength += 5
                    progression()
                elif m_choice == '2':
                    print("You decide to leave the Draughlix, and continue your endless journey.")
                    enemy_encounter_grp += 1
                elif m_choice == '3': # fight is a major wip -pat
                    print(f"\nDraughlix: OH? so you want to challenge me? Have at it then!")
                    global current_enemy
                    draughlix_fight = True
                    current_enemy = current_npc
                    enemy_encounter_grp += 1
                    while draughlix_fight == True:
                        combat(current_enemy)
                        current_enemy = current_npc    
                        if player.is_dead() == True:
                            draughlix_fight = False
            if enc_counter == 3:
                print("treasure") # treasure is a wip sorry -pat
                progression() 
                # Ideally treasure will be implemented once an inventory system has been created -pat
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
            
        

def combat(target_enemy = None):
    inp = input()
    if inp == "Debug":
        print("Entering Debug Mode (Can crash your game, be careful)")
        Console.ConsoleRun()
    # press "enter" to continue turns
    time.sleep(0.1)
#   Set enemy if unnassigned
    if target_enemy == None:
        if enemies == []: return

        global current_enemy
        if current_enemy == -1:
            current_enemy = random.randrange(len(enemies))
            print(f"You encountered a {enemies[current_enemy].name.capitalize()}\n")
            time.sleep(0.1)
            for s in StatusEffect:
                player.status[s] = 0
            
            
           

        #enemy : Entity = npcs[0]
        enemy : Entity = enemies[current_enemy]
    else:
        enemy = target_enemy
        current_enemy = -2 #-2 will be a custom enemy
        
    
    
    global player_turn
    if player_turn: # IF its the players turn
        print("|| Player's Turn")
#       Health not over max hp check
        if player.health > player.max_hp:
            player.health = player.max_hp
        #       enemy health check
        if enemy.health > enemy.max_hp:
            enemy.health = enemy.max_hp
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
                    global enemy_encounter_grp
                    enemy_encounter_grp = 0

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
        if enemy.status[StatusEffect.RAGE] > 0:
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
                        if enemy.weapon.effect != None:
                            player.apply_status(enemy.weapon.effect, enemy.skill)
                            print(f"{enemy.name.capitalize()}'s attack added {enemy.skill} {enemy.weapon.effect.name} to you!")
                        if enemy.weapon.life_steal > 0:
                            enemy.apply_damage(-enemy.calc_lifesteal())
                            print(f"{enemy.name.capitalize()}'s attack drained {enemy.calc_lifesteal()} health from you!")
                        
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
        

    

while enemies != [] and not player.is_dead()  and enemy_encounter_grp != 0:
    
    
    combat()
    
    if enemy_encounter_grp == 0:
        progression()
if player.is_dead():
    print("You have died!")
### /Game Loop 

input() # end of file pause
