# python_text_game.py
# Authors: Iain, Jun, Robert, Cormac, Andrew, Drew, Patrick
# A small text based adventure game

from ctypes import Array
from enum import Enum
import random
import time
import turtle

# global variable definitions
Poison = random.randint(1, 3)
SuperPoison = random.randint(4, 7)

Duck = {"Name": "Duck", "MaxHP": 5, "HP": 5,  "Damage": random.randint(1,6)}
Crab = {"Name": "Crab", "MaxHP": 10, "HP": 10, "Damage": random.randint(1, 3)}
Bee = {"Name": "Bee", "MaxHP": 4, "HP": 4, "Damage": random.randint(1, 2), "StatusFx": Poison}
Trout = {"Name": "Trout", "MaxHP": 7, "HP": 7, "Damage": random.randint(2, 5)}
HawkEye = {"Name": "Hawk Eye", "MaxHP": 7, "HP": 7, "Damage": random.randint(3, 4)}

Enemies = [Duck, Crab, Bee, Trout, HawkEye]
PlayerHP = 20
# class definitions
class Entity:
    def __init__(self, args):
        health
        stamina
        strength
        inventory

class Player(Entity):
    def __init__(self, args: Array) -> None:
        self.health = args["health"]

#       Init empty inventory
        self.inventory = {
            "weapons": [],
            "accessories": [],
            "consumables": []
        }

player = Player({"health": 10})
print(player.health)


# input validation

# inventory

# action loop
#Im going to work on this ~Cormac
# game loop
def Combat():
	print("You encountered a "+ str(Enemies[random.randrange(len(Enemies))]["Name"])+ "\n")
Combat()
input() # end of file pause
