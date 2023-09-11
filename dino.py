import random
class Dino:
    """
    The `Dino` class represents a dinosaur character in your game or simulation.

    Attributes:
    - name (str): The name of the dinosaur.
    - health (int): The current health points of the dinosaur.
    - attacks (list of lists): A list of available attack moves, each represented as [attack_name, damage].

    Methods:
    - choose_random_attack(): Randomly selects an attack move from the available list of attacks.
    - attack(robot): Initiates an attack on a robot character, deducting health points based on the selected attack.

    Example Usage:
    >>> dino = Dino("T-Rex")
    >>> random_attack = dino.choose_random_attack()
    >>> dino.attack(robot)
    """

    def __init__(self, name):
        """
        Initializes a dinosaur character with a given name and default health and attacks.

        Parameters:
        - name (str): The name of the dinosaur.
        """
        self.name = name
        self.health = 1000
        self.attacks = [['claws', 25], ['charge', 50], ['bite', 75]]

    def choose_random_attack(self):
        """
        Randomly selects an attack move from the available list of attacks.

        Returns:
        list: A randomly selected attack move in the format [attack_name, damage].

        This method allows the dinosaur to choose a random attack from its available repertoire.
        """
        random_attack = random.choice(self.attacks)
        return random_attack

    def attack(self, robot):
        """
        Initiates an attack on a robot character, deducting health points based on the selected attack.

        Parameters:
        robot (Robot): The robot character that the dinosaur is attacking.

        This method initiates an attack by selecting a random attack move and deducting health points from the robot.
        It also prints a message describing the attack.
        """
        attack = self.choose_random_attack()
        print(f'{self.name} attacks {robot.name} with a {attack[0]} that deals {attack[1]} damage.')
        robot.health -= attack[1]
