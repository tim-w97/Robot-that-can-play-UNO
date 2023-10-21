from game_logic import *
import keyboard

class GameTest:

    #def __init__(self,player_one,player_two):
    #    self.player_one = player_one
    #    self.player_two = player_two
    
    def test_func(self):
        card_stack_p1 = CardStack([UnoCard(1,Color.RED),UnoCard(7,Color.GREEN),UnoCard(5,Color.BLUE)])
        p1 = Player("John Doe",card_stack_p1)
        p1.add_card(UnoCard(2,Color.YELLOW))
        p1.remove_card(UnoCard(2,Color.YELLOW))
        print(f'Card count of player {p1.name} = {p1.get_card_count()}.')

    def run_game(self):
        while(not keyboard.is_pressed('q')):
            self.test_func()

player_1 = Player("John Doe",CardStack([UnoCard(1,Color.RED),UnoCard(7,Color.GREEN),UnoCard(5,Color.BLUE)]))
player_2 = Player("John Doe",CardStack([UnoCard(1,Color.RED),UnoCard(7,Color.GREEN),UnoCard(5,Color.BLUE)]))
test_game = GameTest(player_1,player_2)
test_game.run_game()