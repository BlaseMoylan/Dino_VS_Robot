
class Dino:
    def _init_(self,name,attack_power):
        self.name=name
        self.attack_power=attack_power
        self.health=100
    def attack(self,robot):
        robot.health=robot.health-self.attack_power
        return robot.health