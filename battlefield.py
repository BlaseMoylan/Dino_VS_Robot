from robot import Robot
from dino import Dino
class Battlefield:
    def __init__(self):
        self.display_welcome()
        self.robot=Robot(input('what is the robot name? '))
        self.dino=Dino(input('What is the dino name? '),25)
    def run_game(self):
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('Welcome to Robot VS Dino!\nloading in Battlefield...')

    def battle_phase(self):
        while self.dino.health>0 and self.robot.health>0:
                self.dino.attack(self.robot)
                self.robot.attack(self.dino)
                print(f'{self.dino.name} health is: {self.dino.health}\n{self.robot.name} health is: {self.robot.health}')

    def display_winner(self):
        if self.dino.health>0:
            print(f'The Winner Is: {self.dino.name}')
        else:
            print(f'The winner is: {self.robot.name}')