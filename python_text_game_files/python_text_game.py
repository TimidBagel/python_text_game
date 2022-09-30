# python_text_game.py
# Authors: Iain, Jun, Robert, Cormac, Andrew, Drew
# A small text based adventure game

from ctypes import Array
from enum import Enum
import random
import time
import turtle

# global variable definitions
Duck = {"Name": "Duck", "MaxHP": 5, "HP": 5,  "Damage": random.randint(1,6)}
Crab = {"Name": "Crab", "MaxHP": 10, "HP": 10, "Damage": random.randint(1, 3)}

Enemies = [Duck, Crab]
PlayerHP = 20
# class definitions
class Entity:
    def __init__(self, args):
        self.health
        self.stamina
        self.strength
        self.inventory

class Player(Entity):
    def __init__(self, args) -> None:
        self.health = args["health"]
        self.stamina = args["stamina"]
        self.strength = args["strength"]

#       Init empty inventory
        self.inventory = {
            "weapons": [],
            "accessories": [],
            "consumables": []
        }

player = Player({"health": 20, "stamina": 10, "strength": 10})
print(player.health)

# misc
def sort_items(items_dict):
    new_dict = {"weapons": [], "accessories": [], "consumables": []}


def drop_loot(entity, player):
    dropped = entity.inventory

# input validation

# inventory

# action loop
#Im going to work on this ~Cormac
# game loop
def Combat():
	print("You encountered a "+ str(Enemies[random.randrange(len(Enemies))]["Name"])+ "\n")
Combat()
input() # end of file pause
