from game_classes import *

#This class is just for testing the game logic itself and the classes and methodes inside game_logic.py#

player_1 = Player("John Doe",CardStack([UnoCard(1,Color.RED),UnoCard(4,Color.GREEN)]))
player_2 = Player("Jane Doe",CardStack([UnoCard(1,Color.RED),UnoCard(7,Color.GREEN),UnoCard(5,Color.BLUE)]))
main_stack = CardStack([UnoCard(4,Color.RED),UnoCard(3,Color.GREEN)])
test_game = Game(player_1,player_2,main_stack)
test_game.run_game()
