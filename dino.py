import random
class Dino:
    def __init__(self,name):
        self.name=name
        self.health=1000
        self.attacks=[['claws',25],['charge',50],['bite',75]]

    def choose_random_attack(self):
        random_attack= random.choice(self.attacks)
        return random_attack

    def attack(self,robot):
        attack=self.choose_random_attack()
        print(f'{self.name} attacks {robot.name} with a {attack[0]} that deals {attack[1]} damage.')
        robot.health=robot.health-attack[1]
