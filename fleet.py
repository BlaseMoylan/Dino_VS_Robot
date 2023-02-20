from robot import Robot
class Fleet:
    def robots(self):
        num=True
        while num==True:
            num_of_robots=input('how many Robots do you want? ')
            if num_of_robots.isnumeric()==True:
                num=False
            else:
                print('You did not enter in only numbers!try again!')
        number=int(num_of_robots)
        list_of_robots=[]
        count=0
        while count<number:
            list_of_robots.append(Robot(input('what is the robot name? ')))
            count+=1
        return list_of_robots