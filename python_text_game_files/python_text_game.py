# python_text_game.py
# Authors: Iain, Jun, Robert, Cormac, Andrew, Drew
# A small text based adventure game

from ctypes import Array
from enum import Enum
import random
import time
import turtle

# global variable definitions

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

# game loop

input() # end of file pause
