# Player.py

from typing import Dict
from Entity import Entity

class Player(Entity):
    def __init__(self, args: Dict) -> None:
        self.health = args["health"]
        self.stamina = args["stamina"]
        self.strength = args["strength"]

#       Init empty inventory
        self.inventory = {
            "weapons": [],
            "accessories": [],
            "consumables": []
        }