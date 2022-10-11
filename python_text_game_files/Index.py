# Index.py
# Authors: Iain, Jun, Robert, Cormac, Andrew, Drew, Ben, Patrick
# A Small Text Based Adventure Game

### NOTES ###
# - Classes are defined as Modules. Meaning they are declared in seperate files. Ie `Player.py` and `Entity.py`
#   which are imported using `from ClassName import ClassName`
# - ALWAYS use snake_case when referring to variables and functions
# - ALWAYS Use PascalCase for Objects and Classes
## /NOTES ###
#hi
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

global enemy_encounter_grp
enemy_encounter_grp : int = 1

global enc_counter
enc_counter = random.randint(1, 3)

global npc_encounters
npc_encounters : int = 1
global player_turn # This is used to keep track if the last turn was the players or not
player_turn = True

global enemies
global npcs
enemies = []
npcs = []

crab = Entity({
    "name": "crab",
    "health": 20, 
    "stamina": 10, 
    "strength": 5,
    "poison": 0,
    "skill": 2,
    "actions": [EntityActions.STRIKE.value, EntityActions.ADD_POISON.value],
    "weapon_effect": None,
    "max_stamina": 10,
    "block_amt": 0
    
    
})

goose = Entity({
    "name": "goose",
    "health": 30, 
    "stamina": 5, 
    "strength": 8,
    "poison": 0,
    "skill": 1,
    "actions": [EntityActions.STRIKE.value],
    "weapon_effect": StatusEffect.BLEED,
    "max_stamina": 5,
    "block_amt": 0
    
})
turtle = Entity({
    "name": "turtle",
    "health": 50, 
    "stamina": 20, 
    "strength": 1,
    "poison": 0,
    "skill": 12,
    "actions": [EntityActions.STRIKE.value, EntityActions.HEAL.value, EntityActions.BLOCK.value],
    "weapon_effect": None,
    "max_stamina": 20,
    "block_amt": 5
    
})
enemies.append(crab)
enemies.append(goose)
enemies.append(turtle)

fred = Entity({
    "name": "fred",
    "health": 9001,
    "stamina": 9001,
    "strength": 9001,
    "poison": 9001,
    "skill": 9001,
    "actions": [EntityActions.STRIKE.value, EntityActions.HEAL.value],
    "weapon_effect": None,
    "max_stamina": 9001,
    "block_amt": 0
    
})
martyr = Entity({
    "name": "martyr",
    "health": 90,
    "stamina": 20,
    "strength": 3,
    "poison": 4,
    "skill": 10,
    "actions": [EntityActions.STRIKE.value, EntityActions.BLOCK.value],
    "weapon_effect": StatusEffect.BLEED,
    "max_stamina": 20,
    "block_amt": 1,
})
npcs.append(fred)
npcs.append(martyr)

player = Entity({
    "name": "player",
    "health": 2000, 
    "stamina": 100000, 
    "strength": 2000000,
    "poison": 0,
    "skill": 5,
    "actions": [EntityActions.STRIKE, EntityActions.BLOCK],
    "weapon_effect": None,
    "max_stamina": 10,
    "block_amt": 3
     
})
### /Global Variables 


### Input Validation 

### /Input Validation 



### Inventory 

### /Inventory 



### Action Loop 
def progression(): #progression loop wip -p
    global enemy_encounter_grp
    global npc_encounters
    global npcs
    global current_npc
    if enemy_encounter_grp == 0:
        input()
        global enc_counter
        enc_counter = random.randint(1, 3)
        print(f"after fighting through the seemingly endless amounts of animals you have come across...")
        if enc_counter == 1:
            print("another enemy!")
            combat()
        if enc_counter == 2:
            npc_encounters = npc_encounters
            if npc_encounters == 1:
                current_npc = npcs(martyr)
                print(f"you have come across the {current_npc.name.capitalize()}")
                has_chosen = False
                while has_chosen == False:
                    m_choice = input(f"""The {current_npc.name.capitalize()} has given you a deal you can gain more power in exchange for your life force... \n
                    do you 
                    1) accept - 10 health for +5 damage
                    2) decline (move on)
                    3) fight the martyr""")
        if enc_counter == 3:
            print("treasure")
### /Action Loop 


### Game Loop 
def display_entity_combat_info(entities):
    print()
    for entity in entities:
        time.sleep(0.01)
        print(f"{entity.name.capitalize()}:")
        time.sleep(0.01)
        print(f"| Health: {str(entity.health)}")
        time.sleep(0.01)
        print(f"| Stamina: {str(entity.stamina)}\n")

def combat():
    input() # press "enter" to continue turns
    time.sleep(0.1)
#   Set enemy if unnassigned

    if enemies == []: return

    global current_enemy
    if current_enemy == -1:
        current_enemy = random.randrange(len(enemies))
        print(f"You encountered a {enemies[current_enemy].name.capitalize()}\n")
        time.sleep(0.1)
       

    #enemy : Entity = npcs[0]
    enemy : Entity = enemies[current_enemy]
    
    global player_turn
    if player_turn: # IF its the players turn
        print("|| Player's Turn")
        
#       Poison check
        
        if bool(player.status[StatusEffect.POISON] > 0):
            player.call_status(StatusEffect.POISON, 1)
            print(f"\nYou took 1 damage from poison. You now have {player.health} health remaining and {player.status[StatusEffect.POISON]} turns of poison remaining")
            player.status[StatusEffect.POISON] -= 1
            time.sleep(0.01)
        #Bleed Check
       

        if player.stamina < player.max_stamina:
            player.stamina += 1
            #We can code in a max stamina stat later as well as a stamina recovery stat you guys don't like to have a ton a variables floating around ~Kit
            #Ive added max stamina ~Kit

        display_entity_combat_info([player, enemy])
        time.sleep(0.01)
        player.block = 0
        print("What will you do?\n")
        time.sleep(0.01)
        print("Player Actions:")
        time.sleep(0.01)
        for action in player.actions:
            print(f"| {action.value}: {action.name.lower().capitalize()}")
            time.sleep(0.01)

    #   Replace with `input_int` when `InputValidation` is made ~Ben
      
        action = input_int("Choose an Action: ")
        print("")

        match action:
            case EntityActions.STRIKE.value:
                if player.stamina > 2:
                    dmg = player.strength - enemy.block
                    if dmg < 1:
                        dmg = 0
                    enemy.apply_damage(dmg) 
                   
                    print(f"Struck {enemy.name.capitalize()} with {dmg} damage")
                    time.sleep(0.01)
                    print(f"{enemy.name.capitalize()} now has {enemy.health} Health")
                    time.sleep(0.01)
                    if bool(player.status[StatusEffect.BLEED] > 0):
                        print(f"Your rapid movements worsened your bleeding.")
                        time.sleep(0.01)
                        player.call_status(StatusEffect.BLEED, 1)
                        print(f"You took 1 damage from bleeding. You now have {player.health} health remaining")
                        time.sleep(0.01)
                        player.status[StatusEffect.BLEED] += 1
                    player.stamina -= 3
                else:
                    print("You are too tired to take that action!")
                    
                if enemy.is_dead():
                    print(f"\n{enemy.name.capitalize()} has fallen in battle")
                    enemies.remove(enemy)
                    current_enemy -= 1
                    global enemy_encounter_grp
                    enemy_encounter_grp -= 1

                    for s in StatusEffect:
                        player.status[s] = 0
                    player.stamina = 10
            case EntityActions.BLOCK.value:
                print(f"You added {player.block_amt} block to self!")
                time.sleep(0.01)
                player.block += player.block_amt
                if bool(player.status[StatusEffect.BLEED] > 0):
                    print(f"Your resting lessened your bleeding.")
                    player.status[StatusEffect.BLEED] -= 4
                    if player.status[StatusEffect.BLEED] < 0:
                        player.status[StatusEffect.BLEED] = 0

#       End Player Turn
        if not enemy.is_dead():
            player_turn = False
        
    else: # IF its the enemies turn
        print("|| Enemy Turn")
        enemy.block = 0
        if enemy.stamina < enemy.max_stamina:
            enemy.stamina += 1
      
        enem_action = random.choice((enemy.actions))
        if enemy.stamina > 2: 
            
            match enem_action:
                case EntityActions.STRIKE.value:
                    dmg = enemy.strength - player.block
                    if dmg < 1:
                        dmg = 0
                    player.apply_damage(dmg) 
                      
                    print(f"{enemy.name.capitalize()} hit you for {dmg} damage. You now have {player.health} health left")
                    if enemy.weapon_effect != None:
                        player.apply_status(enemy.weapon_effect, enemy.skill)
                        print(f"{enemy.name.capitalize()}'s attack added {enemy.skill} {enemy.weapon_effect.name} to you!")
                        #I will try and find a way so enemy attacks can have more than one extra effect, will probably do something with a for loop and such ~Kit
                    enemy.stamina -= 3
                        
                   
                case EntityActions.ADD_POISON.value:
                    # We should make an `add_status` function to `Entity`
                    # I want a bleed status that deals damage when you hit something or use a skill ~Ben
                    #Me Too! I'll do that  ~Kit
                    
                    player.apply_status(StatusEffect.POISON, enemy.skill)
                    print(f"{enemy.name.capitalize()} spit at you and added {enemy.skill} poison!")
                    enemy.stamina -= 2
                        
                case EntityActions.HEAL.value:
                    enemy.apply_damage(-enemy.skill) #Using negative attack damage for healing Big brain ~Kit
                    print(f"{enemy.name.capitalize()} healed for {enemy.skill} damage. It now has {enemy.health} health left")
                    enemy.stamina -= 4
                case EntityActions.BLOCK.value:
                    enemy.block += enemy.block_amt
                    print(f"{enemy.name.capitalize()} added {enemy.block_amt} block to self!")
                
            if enemy.stamina < 0:
                enemy.stamina = 0
            
        else:
            print(f"{enemy.name.capitalize()} is too tired to act!")
#       End Enemy Turn
        player_turn = True

    

while enemies != [] and not player.is_dead() and enemy_encounter_grp != 0:
    combat()
if enemy_encounter_grp == 0:
    progression()
if player.is_dead():
    print("You have died!")
### /Game Loop 

input() # end of file pause













#Old Enemy Logic. Saving it here in case I screw up

##       
