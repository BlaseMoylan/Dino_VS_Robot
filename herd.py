from dino import Dino
class Herd:
    
    def dinos(self):
        num=True
        while num==True:
            num_of_dinos=input('how many dinos do you want? ')
            if num_of_dinos.isnumeric()==True:
                num=False
            else:
                print('You did not enter in only numbers!try again!')
        number=int(num_of_dinos)
        list_of_dinos=[]
        count=0
        while count<number:
            list_of_dinos.append(Dino(input('what is the dino name? ')))
            count+=1
        return list_of_dinos