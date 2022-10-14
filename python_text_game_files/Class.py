from array import array

# Classes have pros and cons for various attributes
class Class:
    def __init__(self, args) -> None:
        self.name = args["name"]
        self.health : int = args["health"]
        self.stamina : int = args["stamina"]
        self.strength : int = args["strength"]

        self.skill : int = args["skill"]
        
        self.raw : dict = args

peasant = Class({
    "name": "Peasant",
    "health": 0,
    "stamina": 0,
    "strength": 0,
    "skill": 0
})

soldier = Class({
    "name": "Soldier",
    "health": 5,
    "stamina": 5,
    "strength": 5,
    "skill": 2
})

mage = Class({
    "name": "Mage",
    "health": -2,
    "stamina": 5,
    "strength": -6,
    "skill": 10
})

classes = []

classes.append(peasant)
classes.append(soldier)
classes.append(mage)