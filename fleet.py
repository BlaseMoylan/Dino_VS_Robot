from robot import Robot
class Fleet:
    """
    The `Fleet` class represents a group of robots.
    
    Attributes:
    None
    
    Methods:
    - robots(): Creates a list of robot objects based on user input for the number and names of robots.
    
    Example Usage:
    >>> fleet = Fleet()
    >>> robots = fleet.robots()
    """

    def robots(self):
        """
        Creates a list of robot objects based on user input for the number and names of robots.
        
        Returns:
        list: A list of robot objects.
        
        This method prompts the user for the number of robots they want and their names.
        It ensures that the user input is valid (numeric for the number of robots).
        It then creates and returns a list of robot objects with the specified names.
        """
        num = True
        while num:
            num_of_robots = input('How many robots do you want? ')
            if num_of_robots.isnumeric():
                num = False
            else:
                print('You did not enter only numbers! Try again!')
        
        number = int(num_of_robots)
        list_of_robots = []
        count = 0
        
        while count < number:
            list_of_robots.append(Robot(input('What is the robot name? ')))
            count += 1
        
        return list_of_robots