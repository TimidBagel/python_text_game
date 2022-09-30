# python_text_game.py
# Authors: Iain, Jun, Robert, Cormac, Andrew
# A small text based adventure game

import random
import time
import turtle

# global variable definitions
Duck = {"Name": "Duck", "MaxHP": 5, "HP": 5,  "Damage": random.randint(1,6)}
Crab = {"Name": "Crab", "MaxHP": 10, "HP": 10, "Damage": random.randint(1, 3)}

Enemies = [Duck, Crab]
PlayerHP = 20
# class definitions


# input validation

# inventory

# action loop
#Im going to work on this ~Cormac
# game loop
def Combat():
	print("You encountered a "+ str(Enemies[random.randrange(len(Enemies))]["Name"])+ "\n")
Combat()
input() # end of file pause
