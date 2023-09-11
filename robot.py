from arsonal import Arsonal
class Robot:
    """
    The `Robot` class represents a robot character in the Robot vs. Dino game.

    Attributes:
    - name (str): The name of the robot.
    - health (int): The current health points of the robot.
    - weapons (Arsenal): The collection of weapons available to the robot.

    Methods:
    - __init__(name): Initializes a robot character with a given name, default health, and an arsenal of weapons.
    - attack(dino): Initiates an attack on a dinosaur character, deducting health points based on the chosen weapon.
    - show_weapon_options(): Displays the available weapon options for the robot.
    - choose_weapon(): Allows the robot to choose a weapon from the available options.

    Example Usage:
    >>> robot = Robot("R2-D2")
    >>> robot.attack(dino)
    >>> robot.show_weapon_options()
    >>> chosen_weapon = robot.choose_weapon()
    """

    def __init__(self, name):
        """
        Initializes a robot character with a given name, default health, and an arsenal of weapons.

        Parameters:
        - name (str): The name of the robot.
        """
        self.name = name
        self.health = 100
        self.weapons = Arsenal()

    def attack(self, dino):
        """
        Initiates an attack on a dinosaur character, deducting health points based on the chosen weapon.

        Parameters:
        - dino (Dino): The dinosaur character that the robot is attacking.

        This method allows the robot to select a weapon, perform an attack, and deduct health points from the dinosaur.
        """
        dino.health -= self.choose_weapon().attack_power

    def show_weapon_options(self):
        """
        Displays the available weapon options for the robot.

        This method prints a list of available weapons and their corresponding index to the console.
        """
        index = 0
        for weapon in self.weapons.weapons:
            print(f"{index}: {weapon.name}")
            index += 1

    def choose_weapon(self):
        """
        Allows the robot to choose a weapon from the available options.

        Returns:
        Weapon: The chosen weapon object.

        This method displays available weapon options to the robot and accepts user input to select a weapon.
        It returns the chosen weapon object for use in an attack.
        """
        self.show_weapon_options()
        user_input = int(input("Please select your weapon option!"))
        
        return self.weapons.weapons[user_input]




