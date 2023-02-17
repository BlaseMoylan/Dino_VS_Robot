from weapon import Weapon
class Robot:
    def __init__(self,name):
        self.name=name
        self.health=100
        self.active_weapon=Weapon('destroyer',50)
    def attack(self,dino):
        dino.health=dino.health-self.active_weapon.attack_power
        return dino.health
        #print(health)
