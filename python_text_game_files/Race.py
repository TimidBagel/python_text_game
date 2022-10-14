from array import array

# Races have pros and cons for various attributes
class Race:
    def __init__(self, args) -> None:
        self.name = args["name"]
        self.health : int = args["health"]
        self.stamina : int = args["stamina"]
        self.strength : int = args["strength"]
        
        self.raw : dict = args