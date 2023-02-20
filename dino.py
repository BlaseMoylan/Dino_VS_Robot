import random
class Dino:
    def __init__(self,name):
        self.name=name
        self.health=1000
    def attack(self,robot):
        claws=25
        charge=50
        bite=75
        attack_names=['claws','charge','bite']
        attack=[claws,charge,bite]
        attack_damage=random.choice(attack)
        for i in attack:
            if i==attack_damage:
                index=attack.index(i)
                name=attack_names[index]
                print(f'{self.name} used {name}')
        robot.health=robot.health-attack_damage
