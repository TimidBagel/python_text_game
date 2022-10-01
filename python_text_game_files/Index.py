# Index.py
# Authors: Iain, Jun, Robert, Cormac, Andrew, Drew, Ben
# A Small Text Based Adventure Game

### NOTES ###
# - Classes are defined as Modules. Meaning they are declared in seperate files. Ie `Player.py` and `Entity.py`
#   which are imported using `from ClassName import ClassName`
# - ALWAYS use snake_case when referring to variables and functions
# - ALWAYS Use PascalCase for Objects and Classes
## /NOTES ###


from ctypes import Array
from enum import Enum
import random
import time
import turtle

### Scripted Modules 
from Player import Player
from Entity import Entity
from Entity import Enemy





### Global Variables
#We don't really need these any more (See how we declare enemies below) They might be good for reference tho so ill just comment them out ~Kit
#duck = {"name": "duck", "max_hp": 5, "hp": 5,  "damage": random.randint(1,6)}
#crab = {"name": "crab", "max_hp": 10, "hp": 10, "damage": random.randint(1, 3)}

enemies = []
### /Global Variables 


### Input Validation 

### /Input Validation 



### Inventory 

### /Inventory 



### Action Loop 
# I'm going to work on this ~Cormac
### /Action Loop 
#Attack Actions ~Kit
#This method probably sucks someone find a better version ~Kit
def hit_low():
    return {"Hurt": random.randint(1,3)}
def heal_low():
    return {"Heal": random.randint(2,4)}
crab_ai = [hit_low(), heal_low()]

player = Player({"health": 20, "stamina": 10, "strength": 10})
print(player.health)

crab = Enemy({"health": 15, "Name": "Crab", "AI": crab_ai})
enemies.append(crab)


### Game Loop 
def combat():
    chosen_enemy = enemies[random.randrange(len(enemies))]
    print("You encountered a "+ chosen_enemy.Name+ " it has " + str(chosen_enemy.health) + " Health\n")
    Inp = input("What would you like to do?\n1. Strike \n2. Block\n")
    enem_act = random.choice(chosen_enemy.AI)
    #Sorry about the constant if checks but I couldn't see a way around it ~Kit
    if "Hurt" in enem_act:
         print(chosen_enemy.Name +" attacked you for " + str(enem_act["Hurt"]) + " Damage\n")
         player.health -= enem_act["Hurt"]
    if "Heal" in enem_act:
        print(chosen_enemy.Name +" healed for " + str(enem_act["Heal"]) + " Damage. It now has " + str(chosen_enemy.health) + " Health")
        #We will need to also add max HP so healing enemies don't gain copius amounts of health. (Same for the player)
        chosen_enemy.health += enem_act["Heal"]
combat()
### /Game Loop 

input() # end of file pause
