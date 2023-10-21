from game_logic import *
import keyboard

class GameTest:

    def __init__(self,player_one,player_two,main_stack):
        self.player_one = player_one
        self.player_two = player_two
        self.main_stack = main_stack
    
    def test_func(self):
        card_stack_p1 = CardStack([UnoCard(1,Color.RED),UnoCard(7,Color.GREEN),UnoCard(5,Color.BLUE)])
        p1 = Player("John Doe",card_stack_p1)
        p1.add_card(UnoCard(2,Color.YELLOW))
        p1.remove_card(UnoCard(2,Color.YELLOW))
        print(f'Card count of player {p1.name} = {p1.get_card_count()}.')

    def run_game(self):
        while(not keyboard.is_pressed('q')):
            pass

player_1 = Player("John Doe",CardStack([UnoCard(1,Color.RED),UnoCard(7,Color.GREEN),UnoCard(5,Color.BLUE)]))
player_2 = Player("Jane Doe",CardStack([UnoCard(1,Color.RED),UnoCard(7,Color.GREEN),UnoCard(5,Color.BLUE)]))
main_stack = CardStack([UnoCard(1,Color.RED)])
test_game = GameTest(player_1,player_2,main_stack)


print(player_1.play_card(UnoCard(1,Color.RED)).get_color())
#test_game.run_game()