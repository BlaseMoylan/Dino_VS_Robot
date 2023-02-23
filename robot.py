from arsonal import Arsonal
class Robot:
    def __init__(self,name):
        self.name=name
        self.health=100
        self.weapons = Arsonal()
    
    def attack(self,dino):
        dino.health=dino.health-self.choose_weapon().attack_power

    def show_weapon_options(self):
        index = 0
        for weapon in self.weapons.weapons:
            print(f"{index}: {weapon.name}")
            index += 1


    def choose_weapon(self):
        self.show_weapon_options()
        user_input = int(input("Please select your weapon option!"))
        
        return self.weapons.weapons[user_input]




