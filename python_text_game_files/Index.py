# python_text_game.py
# Authors: Iain, Jun, Robert, Cormac, Andrew, Drew
# A small text based adventure game

from ctypes import Array
from enum import Enum
import random
import time
import turtle

# Scripted Modules
from Player import Player

# global variable definitions
Duck = {"Name": "Duck", "MaxHP": 5, "HP": 5,  "Damage": random.randint(1,6)}
Crab = {"Name": "Crab", "MaxHP": 10, "HP": 10, "Damage": random.randint(1, 3)}
EnemyNames = ["Crab", "Bee", "Duck", "Trout"]
Enemies = []
PlayerHP = 20
# class definitions

class Enemy(Entity):
    def __init__(self, args: Array) -> None:
        self.health = args["health"]
        self.Name = args["Name"]
        #A list of all the acitons the enemy can do
        self.AI = args["AI"]



player = Player({"health": 20, "stamina": 10, "strength": 10})
print(player.health)


#Attack Actions ~Kit
#This method probably sucks someone find a better version ~Kit
def Hit():
    return random.randint(2, 5)
NormalFighterAI = [Hit()]

player = Player({"health": 20, "stamina": 10, "strength": 10})
print(player.health)
for i in range(4):
    i = Enemy({"health": random.randint(5, 15), "Name": random.choice(EnemyNames), "AI": NormalFighterAI})
    Enemies.append(i)


print(NormalFighterAI[0]);
# input validation

# inventory

# action loop
#Im going to work on this ~Cormac
# game loop
def Combat():
    chosenEnemy = Enemies[random.randrange(len(Enemies))]
    print("You encountered a "+ chosenEnemy.Name+ " it has " + str(chosenEnemy.health) + " Health\n")
    

Combat()

input() # end of file pause
