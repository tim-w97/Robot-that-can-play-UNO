from game_classes import *
from robotPlayer import RobotPlayer

#This class is just for testing the game logic itself and the classes and methodes inside game_logic.py#

initialCard = UnoCard(3, Color.BLUE)
game = Game(HumanPlayer("Lukas"), RobotPlayer("Rob"), initialCard=initialCard)
game.run_game()