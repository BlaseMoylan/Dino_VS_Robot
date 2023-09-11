
from fleet import Fleet
from herd import Herd

class Battlefield:
    """
    The `Battlefield` class represents the main battleground for the Robot vs. Dino game.

    Attributes:
    None

    Methods:
    - __init__(): Initializes the battlefield, displays a welcome message, and creates fleets of robots and dinosaurs.
    - run_game(): Starts the game by displaying the winner of the battle phase.
    - display_welcome(): Displays a welcome message when the game starts.
    - battle_phase(): Simulates the battle phase of the game, where robots and dinosaurs engage in combat.
    - display_winner(): Displays the winner of the game after the battle phase is complete.

    Example Usage:
    >>> battlefield = Battlefield()
    >>> battlefield.run_game()
    """

    def __init__(self):
        """
        Initializes the battlefield, displays a welcome message, and creates fleets of robots and dinosaurs.
        """
        self.display_welcome()
        self.robots = Fleet()
        self.dinos = Herd()

    def run_game(self):
        """
        Starts the game by displaying the winner of the battle phase.
        """
        self.display_winner()

    def display_welcome(self):
        """
        Displays a welcome message when the game starts.
        """
        print('Welcome to Robot VS Dino!\nLoading in Battlefield...')

    def battle_phase(self):
        """
        Simulates the battle phase of the game, where robots and dinosaurs engage in combat.

        Returns:
        str: The winner of the battle phase ('dinos' or 'robots').

        This method initiates the battle phase, where robots and dinosaurs take turns attacking each other.
        It continues until one of the fleets is defeated.
        """
        dinos = self.dinos.dinos()
        robots = self.robots.robots()
        num = 0

        while len(dinos) != 0 and len(robots) != 0:
            if len(dinos) < len(robots):
                num = len(dinos)
            elif len(robots) < len(dinos):
                num = len(robots)
            else:
                num = len(robots)

            for n in range(num):
                if n > len(dinos) - 1:
                    n = len(dinos) - 1
                elif n > len(robots) - 1:
                    n = len(robots) - 1
                dino = dinos[n]
                robot = robots[n]
                robot.attack(dino)
                if dino.health > 0:
                    dino.attack(robot)
                print(f'{dino.name} health is: {dino.health}\n{robot.name} health is: {robot.health}')
                if dino.health < 1 and robot.health < 1:
                    dinos.remove(dino)
                    robots.remove(robot)
                elif dino.health < 1:
                    dinos.remove(dino)
                elif robot.health < 1:
                    robots.remove(robot)
        if len(dinos) != 0:
            return 'dinos'
        else:
            return 'robots'

    def display_winner(self):
        """
        Displays the winner of the game after the battle phase is complete.
        """
        winner = self.battle_phase()
        print(f'The winner is: {winner}')