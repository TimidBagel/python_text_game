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






### Global Variables 
duck = {"name": "duck", "max_hp": 5, "hp": 5,  "damage": random.randint(1,6)}
crab = {"name": "crab", "max_hp": 10, "hp": 10, "damage": random.randint(1, 3)}

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
def HitLow():
    return {"Hurt": random.randint(1,3)}
def HealLow():
    return {"Heal": random.randint(2,4)}
CrabAI = [HitLow(), HealLow()]

player = Player({"health": 20, "stamina": 10, "strength": 10})
print(player.health)

Crab = Enemy({"health": 15, "Name": "Crab", "AI": CrabAI})
enemies.append(Crab)


### Game Loop 
def Combat():
    chosenEnemy = enemies[random.randrange(len(enemies))]
    print("You encountered a "+ chosenEnemy.Name+ " it has " + str(chosenEnemy.health) + " Health\n")
    Inp = input("What would you like to do?\n1. Strike \n2. Block\n")
    EnemAct = random.choice(chosenEnemy.AI)
    #Sorry about the constant if checks but I couldn't see a way around it ~Kit
    if "Hurt" in EnemAct:
         print(chosenEnemy.Name +" attacked you for " + str(EnemAct["Hurt"]) + " Damage\n")
         player.health -= EnemAct["Hurt"]
    if "Heal" in EnemAct:
        chosenEnemy.health += EnemAct["Heal"]
        print(chosenEnemy.Name +" healed for " + str(EnemAct["Heal"]) + " Damage. It now has " + str(chosenEnemy.health) + " Health")
        #We will need to also add max HP so healing enemies don't gain copius amounts of health. (Same for the player)
       
Combat()
### /Game Loop 

input() # end of file pause
