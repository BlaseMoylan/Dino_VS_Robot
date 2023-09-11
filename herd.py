from dino import Dino
class Herd:
    """
    The `Herd` class represents a group of dinosaurs.
    
    Attributes:
    None
    
    Methods:
    - dinos(): Creates a list of dinosaur objects based on user input for the number and names of dinosaurs.
    
    Example Usage:
    >>> herd = Herd()
    >>> dinosaurs = herd.dinos()
    """

    def dinos(self):
        """
        Creates a list of dinosaur objects based on user input for the number and names of dinosaurs.
        
        Returns:
        list: A list of dinosaur objects.
        
        This method prompts the user for the number of dinosaurs they want and their names.
        It ensures that the user input is valid (numeric for the number of dinosaurs).
        It then creates and returns a list of dinosaur objects with the specified names.
        """
        num = True
        while num:
            num_of_dinos = input('How many dinos do you want? ')
            if num_of_dinos.isnumeric():
                num = False
            else:
                print('You did not enter only numbers! Try again!')
        
        number = int(num_of_dinos)
        list_of_dinos = []
        count = 0
        
        while count < number:
            list_of_dinos.append(Dino(input('What is the dino name? ')))
            count += 1
        
        return list_of_dinos