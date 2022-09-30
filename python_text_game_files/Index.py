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



### Global Variables 
duck = {"name": "duck", "max_hp": 5, "hp": 5,  "damage": random.randint(1,6)}
crab = {"name": "crab", "max_hp": 10, "hp": 10, "damage": random.randint(1, 3)}

enemies = [duck, crab]
### /Global Variables 


### Input Validation 

### /Input Validation 



### Inventory 

### /Inventory 



### Action Loop 
# I'm going to work on this ~Cormac
### /Action Loop 



### Game Loop 
def Combat():
	print("You encountered a "+ str(Enemies[random.randrange(len(Enemies))]["Name"])+ "\n")
Combat()
### /Game Loop 

input() # end of file pause
