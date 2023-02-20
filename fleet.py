from robot import Robot
class Fleet:
    def robots(self):
        number=int(input('how many Robots do you want? '))
        list_of_robots=[]
        count=0
        while count<number:
            list_of_robots.append(Robot(input('what is the robot name? ')))
            count+=1
        return list_of_robots