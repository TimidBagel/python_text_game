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



player = Player({"health": 20, "stamina": 10, "strength": 10})
print(player.health)


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
Enemies.append(Crab)



# input validation

# inventory

# action loop

# game loop

#I am very very sorry for my spaghetti code ~Kit
def Combat():
    chosenEnemy = Enemies[random.randrange(len(Enemies))]
    print("You encountered a "+ chosenEnemy.Name+ " it has " + str(chosenEnemy.health) + " Health\n")
    Inp = input("What would you like to do?\n1. Strike \n2. Block\n")
    EnemAct = random.choice(chosenEnemy.AI)
    #Sorry about the constant if checks but I couldn't see a way around it ~Kit
    if "Hurt" in EnemAct:
         print(chosenEnemy.Name +" attacked you for " + str(EnemAct["Hurt"]) + " Damage\n")
         player.health -= EnemAct["Hurt"]
    if "Heal" in EnemAct:
        print(chosenEnemy.Name +" healed for " + str(EnemAct["Heal"]) + " Damage. It now has " + str(chosenEnemy.health) + " Health")
        #We will need to also add max HP so healing enemies don't gain copius amounts of health. (Same for the player)
        chosenEnemy.health += EnemAct["Heal"]
    

Combat()
input() # end of file pause
