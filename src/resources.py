# imports
# globala variables
# classes
class Character:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
    
    def __str__(self):
        return f"Name: {self.name}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}"
    
    def take_damage(self, dmg):
        actual_damage = dmg - self.armor

        if actual_damage < 0: actual_damage = 0
        
        if self.health - actual_damage < 0: self.health = 0
        
        else: self.health -= actual_damage

    def attack(self):
        return self.damage
    
    def get_health(self):
        return self.health

    def get_name(self):
        return self.name
class Goblin:

    def __init__(self, id):
        self.id = id
        self.health = 10
        self.damage = 3
        self.armor = 2
    
    def __str__(self):
        return f"ID: {self.id}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}"
    def take_damage(self, dmg):
        actual_damage = dmg - self.armor
        
        if actual_damage < 0: actual_damage = 0

        if self.health - actual_damage < 0: self.health = 0
        
        else: self.health -= actual_damage
    def attack(self):
        return self.damage
    
    def get_health(self):
        return self.health
        
    def get_name(self):
        return f"Goblin #{self.id}"
    
# functions

# main code
