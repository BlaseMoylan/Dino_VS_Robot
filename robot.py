from weapon import Weapon
class Robot:
    def __init__(self,name):
        self.name=name
        self.health=100
        #self.active_weapon()
    def attack(self,dino):
        dino.health=dino.health-self.active_weapon().attack_power
        
    def active_weapon(self):
        lazer=Weapon('Lazer',50)
        Sword=Weapon('Sword',100)
        rockets=Weapon('Rockets',500)
        arsonal=[lazer,Sword,rockets]
        arsonal_names=['Lazer','Sword','Rockets']
        selected_weapon=input(f'please select a weapon to use? {arsonal_names}')
        for i in arsonal_names:
            if selected_weapon==i:
                index=arsonal_names.index(i)
                weapon=arsonal[index]
                return weapon

