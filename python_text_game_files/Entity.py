# Entity.py

class Entity:
    def __init__(self, args) -> None:
        health
        stamina
        strength
        inventory

class Enemy(Entity):
    def __init__(self, args) -> None:
        self.health = args["health"]
        self.Name = args["Name"]
        #A list of all the acitons the enemy can do
        self.AI = args["AI"]
