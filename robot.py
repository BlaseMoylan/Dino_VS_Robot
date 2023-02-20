from arsonal import Arsonal
class Robot:
    def __init__(self,name):
        self.name=name
        self.health=100
        self.weapon=Arsonal()
    def attack(self,dino):
        dino.health=dino.health-self.weapon.active_weapon().attack_power