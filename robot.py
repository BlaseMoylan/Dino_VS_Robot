from weapon import Weapon
class Robot:
    def __init__(self,name):
        self.name=name
        self.health=100
    def attack(self,dino):
        dino.health=dino.health-self.active_weapon().attack_power
        
    def active_weapon(self):
        lazer=Weapon('Lazer',100)
        Sword=Weapon('Sword',250)
        rockets=Weapon('Rockets',500)
        arsonal=[lazer,Sword,rockets]
        arsonal_names=['Lazer','Sword','Rockets']
        name=True
        while name==True:
            selected_weapon=input(f'please select a weapon to use? {arsonal_names}')
            if selected_weapon in arsonal_names:
                name=False
            else:
                print('this is not kone of the options!Please try again!')
        for i in arsonal_names:
            if selected_weapon==i:
                index=arsonal_names.index(i)
                weapon=arsonal[index]
                return weapon

