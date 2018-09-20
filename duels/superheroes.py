import random

class Ability:
    def __init__(self, name, attack_strength):
        # Initialize starting values
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        # Return attack value

        self.attack_low = attack_strength // 2
        self.attack_strength_high = attack_strength

        self.damage_random = random.randint(self.attack_low, self.attack_strength_high)
        self.damage = random.randint(0, self.damage_random)



    def update_attack(self, attack_strength):
        # Update attack value
        self.attack_strength =

class Hero:
    def __init__(self, name):
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        # append ability to self.ability
        self.abilities.append(ability)
