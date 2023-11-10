from enum import Enum

class Color(Enum):

    BLACK = 0
    YELLOW = 1
    RED = 2
    GREEN = 3
    BLUE = 4

class UnoCard:

    def __init__(self, number: int, color: Color):
        self.number = number
        self.color = color
    
    def get_number(self) -> int:
        return self.number
    
    def get_color(self) -> Color:
        return self.color
    
    def to_string(self) -> str:
        return ''.join(f'{str(self.color)} {str(self.number)}')

    def match(self, other: UnoCard):
        return self.color == other.color or self.number == other.number
    
class CardStack:

    def __init__(self, cards: [UnoCard]):
        self.cards = cards
        self.card_amount = len(self.cards)

    def add_card(self, card: UnoCard):
        self.cards.append(card)
        self.card_amount = len(self.cards)

    def remove_card(self, card: UnoCard):
        for i in self.cards:
                if i.number == card.number and i.color == card.color:
                    self.cards.remove(i)
        self.card_amount = len(self.cards)
    
    def pop_specific_card(self, card: UnoCard) -> UnoCard:
        for i in range(len(self.cards)):
                if self.cards[i].number == card.number and self.cards[i].color == card.color:
                    tmp = self.cards.pop(i)
                    self.card_amount = len(self.cards)
                    return tmp
        return None
    
    def get_card(self, card: UnoCard) -> UnoCard:
        for i in range(len(self.cards)):
                if self.cards[i].number == card.number and self.cards[i].color == card.color:
                    return self.cards[i]
        return None
        
    def get_all_cards(self) -> [UnoCard]:
        return self.cards
    
    def cards_to_string(self) -> str:
        return ' '.join(f'{card.to_string()}'for card in self.get_all_cards())

#TODO: Think about the member functions again. A human player don't need to control a stack. A robot does.
# The game does not have to differ between players. But the each player has to signal the game, that they are done
# with their turn.
"""
This class represents a player.
"""
class Player:

    def __init__(self, name: str):
        self.name = name
    
    """
    This method is called from the game and needs to be overwritten.
    """
    def doMove(self) -> bool:
        pass

class HumanPlayer(Player):
    def __init__(self, name: str):
        super(name)

    """
    Just wait for a signal.
    """
    @Overwrite
    def doMove(self) -> bool:
        pass


"""
This is the class to control the game. It is responsible for a game flow.
"""
class Game:

    def __init__(self, *args: [Player]):
        if len(args) < 2: raise Exception("You need at least two players!")
        self.players = args
        self.activePlayer = args[0]

    # Refactored this method in UnoCard
    def match_cards(self, card_1: UnoCard, card_2: UnoCard) -> bool:
        if(card_1.color == card_2.color or card_1.number == card_2.number):
            return True
        return False
    
    def check_winner(self,player)->bool:
        if player.get_card_count() == 0:
            print(f'{player.name} has won the game!')
            self.game_is_over = True
            return self.game_is_over
        else:
            self.game_is_over = False
            return self.game_is_over


    def switch_current_player(self,player):
        self.current_player = player

    def turn(self,player):
        #TODO
        #1. Display current players card
        print(player.cards_to_string)
        #2. Player Input
        #3. Compare there cards with main stack or moved pulled card to player stack
        #4. check if game is over
        #5. if not over switch players

    def run_game(self):
        while True:
            while(not self.game_is_over):
                print(f'gamestate:{self.game_is_over}')
                self.check_winner(self.player_one)
            if input()=='q':
                break
