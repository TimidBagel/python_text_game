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
from InputValidator import input_float, input_int, input_str
from StatusEffect import StatusEffect


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
    "actions": [EntityActions.STRIKE.value, EntityActions.ADD_POISON.value],
    "weapon_effect": None
})

goose = Entity({
    "name": "goose",
    "health": 30, 
    "stamina": 10, 
    "strength": 8,
    "poison": 0,
    "skill": 1,
    "actions": [EntityActions.STRIKE.value],
    "weapon_effect": StatusEffect.BLEED
})
turtle = Entity({
    "name": "turtle",
    "health": 50, 
    "stamina": 10, 
    "strength": 1,
    "poison": 0,
    "skill": 12,
    "actions": [EntityActions.STRIKE.value, EntityActions.HEAL.value],
    "weapon_effect": None
})
enemies.append(crab)
enemies.append(goose)
enemies.append(turtle)

player = Entity({
    "name": "player",
    "health": 20, 
    "stamina": 10, 
    "strength": 10,
    "poison": 0,
    "skill": 5,
    "actions": [EntityActions.STRIKE, EntityActions.BLOCK],
    "weapon_effect": None
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

    if enemies == []: return

    global current_enemy
    if current_enemy == -1:
        current_enemy = random.randrange(len(enemies))
        print(f"You encountered a {enemies[current_enemy].name.capitalize()}\n")
       

    enemy : Entity = enemies[current_enemy]
    
    global player_turn
    if player_turn: # IF its the players turn
        print("|| Players Turn")
        
        print(f"{enemy.name.capitalize()}:")
        print(f"| Health: {str(enemy.health)}")
        
#       Poison check
        
        if bool(player.status[StatusEffect.POISON] > 0):
            player.call_status(StatusEffect.POISON, 1)
            print(f"You took 1 damage from poison. You now have {player.health} health remaining and {player.status[StatusEffect.POISON]} turns of poison remaining")
            player.status[StatusEffect.POISON] -= 1
        #Bleed Check
       
            
        
        print("What will you do?")
        print("Player Actions:")
        for action in player.actions:
            print(f"| {action.value}: {action.name.lower().capitalize()}")

    #   Replace with `input_int` when `InputValidation` is made ~Ben
      
        action = input_int("Choose an Action: ")
        print("")

        match action:
            case EntityActions.STRIKE.value:
                enemy.apply_damage(player.strength)
                print(f"Struck {enemy.name.capitalize()} with {player.strength} damage")
                print(f"{enemy.name.capitalize()} now has {enemy.health} Health")
                if bool(player.status[StatusEffect.BLEED] > 0):
                    print(f"Your rapid movements worsened your bleeding.")
                    player.call_status(StatusEffect.BLEED, 1)
                    print(f"You took 1 damage from bleeding. You now have {player.health} health remaining")
                    player.status[StatusEffect.BLEED] += 1
                if enemy.is_dead():
                    print(f"\n{enemy.name.capitalize()} has fallen in battle")
                    enemies.remove(enemy)
                    current_enemy = -1
                    player_turn = True
            case EntityActions.BLOCK.value:
                print("You chose to block")
                if bool(player.status[StatusEffect.BLEED] > 0):
                    print(f"Your resting lessened your bleeding.")
                    player.status[StatusEffect.BLEED] -= 2

#       End Player Turn
        player_turn = False
    else: # IF its the enemies turn
        print("|| Enemy Turn")
      
        enem_action = random.choice((enemy.actions))
        match enem_action:
            case EntityActions.STRIKE.value:
                player.apply_damage(enemy.strength) 
                #We still need to invent blocks ~Kit
                # I can handle this later ~Ben
                print(f"{enemy.name.capitalize()} hit you for {enemy.strength} damage. You now have {player.health} health left")
                if enemy.weapon_effect != None:
                    player.apply_status(enemy.weapon_effect, enemy.skill)
                    print(f"{enemy.name.capitalize()}'s attack added {enemy.skill} {enemy.weapon_effect.name} to you!")
                    #I will try and find a way so enemy attacks can have more than one extra effect, will probably do something with a for loop and such ~Kit
            case EntityActions.ADD_POISON.value:
                # We should make an `add_status` function to `Entity`
                # I want a bleed status that deals damage when you hit something or use a skill ~Ben
                #Me Too! I'll do that  ~Kit
                
                player.apply_status(StatusEffect.POISON, enemy.skill)
                print(f"{enemy.name.capitalize()} spit at you and added {enemy.skill} poison!")
            case EntityActions.HEAL.value:
                enemy.apply_damage(-enemy.skill) #Using negative attack damage for healing Big brain ~Kit
                print(f"{enemy.name.capitalize()} healed for {enemy.skill} damage. It now has {enemy.health} health left")
#       End Enemy Turn
        player_turn = True

while enemies != [] and not player.is_dead():
    combat()
if player.is_dead():
    print("You have died!")
### /Game Loop 

input() # end of file pause
