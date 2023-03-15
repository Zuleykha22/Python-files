class Weapon:
    metal = 'iron'
    def __init__(self, bullet):
        self.bullet = bullet

class Automat(Weapon):
    power = 25

class Sniper(Weapon):
    power = 15

class Soldier:
    health = 100
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon 
    def fire(self, player):
        player.health = player.health - self.weapon.power
        self.weapon.bullet -= 1

