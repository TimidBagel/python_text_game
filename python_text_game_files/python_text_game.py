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
EnemyNames = ["Crab", "Bee", "Duck", "Trout"]
Enemies = []
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
        self.stamina = args["stamina"]
        self.strength = args["strength"]

#       Init empty inventory
        self.inventory = {
            "weapons": [],
            "accessories": [],
            "consumables": []
        }
class Enemy(Entity):
    def __init__(self, args: Array) -> None:
        self.health = args["health"]
        self.Name = args["Name"]
        #A list of all the acitons the enemy can do
        self.AI = args["AI"]


#Attack Actions ~Kit
#This method probably sucks someone find a better version ~Kit
def Hit():
    return random.randint(2, 5)
def Hunker():
    return random.randint(2,5)
CrabAI = [Hit(), Hunker()]

player = Player({"health": 20, "stamina": 10, "strength": 10})
print(player.health)

Crab = Enemy({"health": 15, "Name": "Crab", "AI": CrabAI})
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
