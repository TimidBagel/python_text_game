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
from Entity import Entity, EntityActions, enemies, npcs
from Race import Race, races, human, halfling, monster
from Class import Class, classes, peasant, soldier, mage
from Item import Item, ItemTypes, ItemWeapon, weapons, consumables
from InputValidator import input_float, input_int, input_str
from StatusEffect import StatusEffect
from FileSystem import write_file, read_file

from Debug import Console
#Alternatively, we can import all the weapons from ITEM ~Kit
from Item import goose_beak, no_weapon, toad_hand, absorbers_wand, blade_of_agony
#I will do the same with enemies
from Entity import crab, turtle, toad, goose, rabbit, dark_sprite, steelblade_squire

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

player = Entity({
    "name": "player",
    "race": human,
    "health": 30, 
    "max_hp": 30,
    "stamina": 15, 
    "strength": 15,
    "poison": 0,
    "skill": 5,
    "actions": [EntityActions.STRIKE, EntityActions.BLOCK],
    "max_stamina": 15,
    "block_amt": 3,
    "Weapon": no_weapon,
    "is_enemy": False
     
})

### /Global Variables 


### Input Validation 

### /Input Validation 

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

            enemy_encounter_grp = 1
            
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
def new_character(character_path):
    print()
    name = input_str("Enter a name for your new character: ")
    
    print("List of available classes:")

    for i in range(len(classes)):
        print(f"{i}. {classes[i].name}")
    
    found = False
    while not found:
        _class = input_str("Enter a class name for your new character: ")

        for i in classes:
            if _class.lower() == i.name.lower():
                char_class = i
                found = True
        
        if not found:
            print(f"Class name '{_class}' not found. Please enter a valid class name.")
        
    
    print("List of available races:")

    for i in range(len(races)):
        print(f"{i}. {races[i].name}")
    
    found = False
    while not found:
        race = input_str("Enter a race name for your new character: ")

        for i in races:
            if race.lower() == i.name.lower():
                char_race = i
                found = True

        if not found:
            print(f"Race name '{race}' not found. Please enter a valid race name.")

    new_character = Entity({
        "name": name,
        "race": char_race,
        "Class": char_class,
        "health": 30 + char_race.health + char_class.health,
        "stamina": 10 + char_race.stamina + char_class.stamina,
        "strength": 10 + char_race.strength + char_class.strength,
        "poison": 0,
        "skill": 5 + char_class.skill,
        "actions": [EntityActions.STRIKE, EntityActions.BLOCK],
        "weapon_effect": None,
        "max_stamina": 10,
        "block_amt": 3,
        "Weapon": no_weapon
    })

    write_file(f"{character_path}{name}.json", new_character.raw)

    print(f"""

Character Information:
    Name: '{new_character.name}'
    Race: '{new_character.race.name}'
   Class: '{new_character.Class.name}'
  Health: {new_character.health}
 Stamina: {new_character.stamina}
Strength: {new_character.strength}
   Skill: {new_character.skill}
    """)

def fetch_character(name): # wip for fetching character files
    character = None
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
    global enemy_encounter_grp
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
           
        player.block = 0
        display_entity_combat_info([player, enemy])
        time.sleep(0.01)
       
        print("What will you do?\n")
        time.sleep(0.01)
        print("Player Actions:")
        time.sleep(0.01)
        for action in player.actions:
            print(f"| {action.value}: {action.name.lower().capitalize()}")
            time.sleep(0.01)

   
      
        action = input_int("Choose an Action: ")
        print("")

        player.take_turn(enemy, action)
          
#       End Player Turn
        if not enemy.is_dead():
            player_turn = False
        else:
            enemy_encounter_grp = 0
            print(f"{enemy.name.capitalize()} has fallen in battle")
            enemies.remove(enemy)
    else: # IF its the enemies turn
        print("|| Enemy Turn")
        if enemy.status[StatusEffect.RAGE] > 0:
            enemy.status[StatusEffect.RAGE] -= 1
        enemy.block = 0
        if enemy.stamina < enemy.max_stamina:
            enemy.stamina += 1
      
        enemy.take_turn(player, random.choice(enemy.actions))
        if enemy.stamina < 0:
            enemy.stamina = 0
            
      
#       End Enemy Turn
        player_turn = True
        
   
    
### Character test
parent_directory = pathlib.Path(__file__).parent.resolve()
character_directory = "characters/"
user_directory = "userdata/"
user_path = os.path.join(parent_directory, user_directory)
character_path = os.path.join(user_path, character_directory)
if not os.path.exists(user_path):
    os.mkdir(user_path)
if not os.path.exists(character_path):
    os.mkdir(character_path)
new_character(character_path)
input()
### /character test

while enemies != [] and not player.is_dead() and enemy_encounter_grp != 0:
    combat()
    
if enemy_encounter_grp == 0:
    progression()
    current_enemy = -1
if player.is_dead():
    print("You have died!")
### /Game Loop 

input() # end of file pause
