from game_classes import *

#This class is just for testing the game logic itself and the classes and methodes inside game_logic.py#

class GameTest:

    def __init__(self,player_one,player_two,main_stack):
        self.player_one = player_one
        self.player_two = player_two
        self.main_stack = main_stack
        self.game_is_over = False

    def set_winner(self,player):
        if player.get_card_count() == 0:
            print(f'{player.name} has won the game!')
            self.game_is_over = True
        else:
            self.game_is_over = False
    
    def test_func_remove_add(self):
        card_stack_p1 = CardStack([UnoCard(1,Color.RED),UnoCard(7,Color.GREEN),UnoCard(5,Color.BLUE)])
        p1 = Player("John Doe",card_stack_p1)
        p1.add_card(UnoCard(2,Color.YELLOW))
        p1.remove_card(UnoCard(2,Color.YELLOW))
        print(f'Card count of player {p1.name} = {p1.get_card_count()}.')

    def run_game(self):
        while True:
            while(not self.game_is_over):
                self.player_one.play_card(UnoCard(1,Color.RED))
                print(self.player_one.get_card_count())
                print(f'gamestate:{self.game_is_over}')
                self.set_winner(self.player_one)
            if input()=='q':
                break



player_1 = Player("John Doe",CardStack([UnoCard(1,Color.RED)]))
player_2 = Player("Jane Doe",CardStack([UnoCard(1,Color.RED),UnoCard(7,Color.GREEN),UnoCard(5,Color.BLUE)]))
main_stack = CardStack([UnoCard(1,Color.RED)])
test_game = GameTest(player_1,player_2,main_stack)
test_game.run_game()
test_game.test_func_remove_add()
