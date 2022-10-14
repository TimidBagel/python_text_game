from array import array

# Races have pros and cons for various attributes
class Race:
    def __init__(self, args) -> None:
        self.name = args["name"]
        self.health : int = args["health"]
        self.stamina : int = args["stamina"]
        self.strength : int = args["strength"]
        
        self.raw : dict = args

human = Race({
    "name": "Human",
    "health": 0,
    "stamina": 0,
    "strength": 0
})

halfling = Race({
    "name": "Halfling",
    "health": 5,
    "stamina": -5,
    "strength": -5
})

monster = Race({
    "name": "Monster",
    "health": 0,
    "stamina": 0,
    "strength": 0
})

races = []

races.append(human)
races.append(halfling)
races.append(monster)