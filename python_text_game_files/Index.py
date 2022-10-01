# Index.py
# Authors: Iain, Jun, Robert, Cormac, Andrew, Drew, Ben
# A Small Text Based Adventure Game

### NOTES ###
# - Classes are defined as Modules. Meaning they are declared in seperate files. Ie `Player.py` and `Entity.py`
#   which are imported using `from ClassName import ClassName`
# - ALWAYS use snake_case when referring to variables and functions
# - ALWAYS Use PascalCase for Objects and Classes
## /NOTES ###

import random
import time
import turtle

### Scripted Modules 
from Entity import Entity, EntityActions
from Item import Item, ItemTypes


### Global Variables
global current_enemy
current_enemy : int = -1

global player_turn # This is used to keep track if the last turn was the players or not
player_turn = True

global enemies
enemies = []

crab = Entity({
    "name": "crab",
    "health": 20, 
    "stamina": 10, 
    "strength": 5,
    "poison": 0,
    "skill": 2,
    "ai": [0, 3]
})

goose = Entity({
    "name": "goose",
    "health": 30, 
    "stamina": 10, 
    "strength": 8,
    "poison": 0,
    "skill": 0,
    "ai": [0]
})
enemies.append(crab)
enemies.append(goose)

player = Entity({
    "name": "player",
    "health": 20, 
    "stamina": 10, 
    "strength": 10,
    "poison": 0,
    "skill": 5,
    "ai": []
})
### /Global Variables 


### Input Validation 

### /Input Validation 



### Inventory 

### /Inventory 



### Action Loop 

### /Action Loop 


### Game Loop 

def combat():
#   Set enemy if unnassigned

    global current_enemy
    if current_enemy == -1:
        current_enemy = random.randrange(len(enemies))
        print(f"You encountered a {enemies[current_enemy].name.capitalize()}\n")
       

    enemy : Entity = enemies[current_enemy]
    
    global player_turn
    if player_turn: # IF its the players turn
        
        print(f"{enemy.name.capitalize()}:")
        print(f"| Health: {str(enemy.health)}")
        if player.poison >= 1:
            player.health -= player.poison
            print(f"You took {player.poison} damage from poison. You now have {player.health} health remaining")
            player.apply_damage(player.poison)
            player.poison -= 1
            if player.health < 1:
                print("You have died!")
                input()
        
            
            #Please contact me if you think poison damage shouldn't scale up and be a hard value ~Kit
        print("What will you do?")
        print("Player Actions:")
        for action in EntityActions:
            print(f"| {action.value}: {action.name.lower().capitalize()}")

    #   Replace with `input_int` when `InputValidation` is made ~Ben
      
        action = int(input("Choose an Action: "))
        print("")

        match action:
            case EntityActions.STRIKE.value:
                enemy.apply_damage(player.strength)
                print(f"Struck {enemy.name.capitalize()} with {player.strength} damage")
                print(f"{enemy.name.capitalize()} now has {enemy.health} Health")
                if enemy.is_dead():
                    print(f"\n{enemy.name.capitalize()} has fallen in battle")
                    enemies.remove(enemy)
                    current_enemy = -1
            case EntityActions.BLOCK.value:
                print("You chose to block")
            case EntityActions.ESCAPE.value:
                print("You chose to block")

#       End Player Turn
        player_turn = False
    else: # IF its the enemies turn
      
        enem_action = random.choice(enemy.ai)
        match enem_action:
            case EntityActions.STRIKE.value:
                player.apply_damage(enemy.strength) #We still need to invent blocks ~Kit
                print(f"{enemy.name.capitalize()} hit you for {enemy.strength} damage. You now have {player.health} health left")
            case EntityActions.ADDPOISON.value:
                player.poison += enemy.skill
                print(f"{enemy.name.capitalize()} spit at you and added {enemy.skill} poison!")
#       End Enemy Turn
        if player.health > 0:
            player_turn = True
        else:
            print("You have died!")
            input()
            
        

while enemies != [] and player.health > 0:
    combat()
### /Game Loop 

input() # end of file pause
