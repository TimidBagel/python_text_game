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