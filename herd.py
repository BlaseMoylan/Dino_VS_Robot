from dino import Dino
class Herd:
    def dinos(self):
        number=int(input('how many dinos do you want? '))
        list_of_dinos=[]
        count=0
        while count<number:
            list_of_dinos.append(Dino(input('what is the dino name? '),25))
            count+=1
        return list_of_dinos