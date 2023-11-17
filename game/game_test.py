from game_classes import *

#This class is just for testing the game logic itself and the classes and methodes inside game_logic.py#

initialCard = UnoCard(2, Color.BLUE)
game = Game(HumanPlayer("Lukas"), HumanPlayer("Anonymous"), initialCard=initialCard)
game.run_game()