
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.display_welcome()
        self.robots=Fleet()
        self.dinos=Herd()

    def run_game(self):
        self.display_winner()

    def display_welcome(self):
        print('Welcome to Robot VS Dino!\nloading in Battlefield...')

    def battle_phase(self):
        dinos=self.dinos.dinos()
        robots=self.robots.robots()
        num=0

        while len(dinos)!=0 and len(robots)!=0:
            if len(dinos)<len(robots):
                num=len(dinos)
            elif len(robots)<len(dinos):
                num=len(robots)
            else:
                num=len(robots)

            for n in range(num):
                if n > len(dinos)-1:
                    n=len(dinos)-1
                elif n > len(robots)-1:
                    n=len(robots)-1
                dino=dinos[n]
                robot=robots[n]
                robot.attack(dino)
                if dino.health>0:
                    dino.attack(robot)
                print(f'{dino.name} health is: {dino.health}\n{robot.name} health is: {robot.health}')
                if dino.health<1 and robot.health<1:
                    dinos.remove(dino)
                    robots.remove(robot)
                elif dino.health<1:
                    dinos.remove(dino)
                elif robot.health<1:
                    robots.remove(robot)
        if len(dinos)!=0:
            return 'dinos'
        else:
            return 'robots'
            

    def display_winner(self):
        winner=self.battle_phase()
        print(f'The winner is: {winner}')