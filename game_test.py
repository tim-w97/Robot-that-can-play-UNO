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
    
    
    def match_cards(self,card_1,card_2)->bool:
        if(card_1.color == card_2.color or card_1.number == card_2.number):
            return True
        return False


    def run_game(self):
        while True:
            while(not self.game_is_over):
                print(self.match_cards(player_1.get_card(UnoCard(4,Color.GREEN)),main_stack.get_card(UnoCard(3,Color.GREEN))))
                print(self.match_cards(player_1.play_card(UnoCard(4,Color.GREEN)),main_stack.pop_specific_card(UnoCard(3,Color.GREEN))))
                print(self.match_cards(player_1.play_card(UnoCard(1,Color.RED)),main_stack.pop_specific_card(UnoCard(4,Color.RED))))
                print(self.player_one.get_card_count())
                print(f'gamestate:{self.game_is_over}')
                self.set_winner(self.player_one)
            if input()=='q':
                break



player_1 = Player("John Doe",CardStack([UnoCard(1,Color.RED),UnoCard(4,Color.GREEN)]))
player_2 = Player("Jane Doe",CardStack([UnoCard(1,Color.RED),UnoCard(7,Color.GREEN),UnoCard(5,Color.BLUE)]))
main_stack = CardStack([UnoCard(4,Color.RED),UnoCard(3,Color.GREEN)])
test_game = GameTest(player_1,player_2,main_stack)
print(test_game.player_one.cardstack.cards_to_string())
#test_game.run_game()
