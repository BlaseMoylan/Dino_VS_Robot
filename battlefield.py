#need to make it work with one Robot and one Dino
#also I want to make a limit on how many times rockets can be used
#also need to make conditionals to take care of wronge input values
#also need to do more testing with edge cases
#then need to refactor and clean up my code


from robot import Robot
from dino import Dino
class Battlefield:
    def __init__(self):
        self.display_welcome()
        # self.robots()
        # self.dinos()
        # self.robot=Robot(input('what is the robot name? '))
        # self.dino=Dino(input('What is the dino name? '),25)
    def run_game(self):
        #self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('Welcome to Robot VS Dino!\nloading in Battlefield...')

    def battle_phase(self):
        dinos=self.dinos()
        robots=self.robots()
        num=0
        if len(dinos)<len(robots):
            num=len(dinos)-1
        elif len(robots)<len(dinos):
            num=len(robots)-1
        # elif len(robots)

        while dinos!=[] and robots!=[]:
            for n in range(num):
                dino=dinos[n]
                robot=robots[n]
                #while self.dino.health>0 and self.robot.health>0:
                dino.attack(robot)
                robot.attack(dino)
                print(f'{dino.name} health is: {dino.health}\n{robot.name} health is: {robot.health}')
                if dino.health<1 and robot.health<1:
                    dinos.remove(dino)
                    robots.remove(robot)
                elif dino.health<1:
                    dinos.remove(dino)
                elif robot.health<1:
                    robots.remove(robot)
        if dinos!=[]:
            return 'dinos'
        else:
            return 'robots'
            

    def display_winner(self):
        winner=self.battle_phase()
        print(f'The winner is: {winner}')
        # if self.dino.health>0:
        #     print(f'The Winner Is: {self.dino.name}')
        # else:
        #     print(f'The winner is: {self.robot.name}')
    
    def robots(self):
        number=int(input('how many Robots do you want? '))
        list_of_robots=[]
        count=0
        while count<number:
            list_of_robots.append(Robot(input('what is the robot name? ')))
            count+=1
        return list_of_robots
    
    def dinos(self):
        number=int(input('how many dinos do you want? '))
        list_of_dinos=[]
        count=0
        while count<number:
            list_of_dinos.append(Dino(input('what is the dino name? '),25))
            count+=1
        return list_of_dinos