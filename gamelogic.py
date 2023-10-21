from enum import Enum

class Color(Enum):
    BLACK = 0
    YELLOW = 1
    RED = 2
    GREEN = 3
    BLUE = 4

class UnoCard:

    def __init__(self,number,color):
        self.number = number
        self.color = color
    
    def get_number(self)->int:
        return self.number
    
    def get_color(self)->Color:
        return self.color
    
class CardStack:

    def __init__(self,cards):
        self.cards = cards
        self.card_amount = len(cards)

    def add_card(self,card):
        self.cards.append(card)
        self.card_amount = len(self.cards)

    def remove_card(self,card):
        for i in self.cards:
                if i.number == card.number and i.color == card.color:
                    self.cards.remove(i)
        self.card_amount = len(self.cards)

class Player:

    def __init__(self,name,cardstack):
        self.name = name
        self.cardstack = cardstack

    def add_card(self,card):
        self.cardstack.add_card(card)
    
    def remove_card(self,card):
        self.cardstack.remove_card(card)
    
    def get_card_count(self) -> int:
        return self.cardstack.card_amount

class Game:
    #if color or number equal...
    #user input move finished...
    #for testing console input/output...
    #two card stacks one for drawing one for field...
    #state...
    #keep track which players turn it is
    #check who is winning
    def __init__(self,player_one,player_two):
        self.player_one = player_one
        self.player_two = player_two

class GameTest:
    pass

def test_func():
    card_stack_p1 = CardStack([UnoCard(1,Color.RED),UnoCard(7,Color.GREEN),UnoCard(5,Color.BLUE)])
    p1 = Player("John Doe",card_stack_p1)
    p1.add_card(UnoCard(2,Color.YELLOW))
    p1.remove_card(UnoCard(2,Color.YELLOW))
    print(f'Card count of player {p1.name} = {p1.get_card_count()}.')

test_func()

