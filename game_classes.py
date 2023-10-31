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
        self.card_amount = len(self.cards)

    def add_card(self,card):
        self.cards.append(card)
        self.card_amount = len(self.cards)

    def remove_card(self,card):
        for i in self.cards:
                if i.number == card.number and i.color == card.color:
                    self.cards.remove(i)
        self.card_amount = len(self.cards)
    
    def pop_card(self,card) -> UnoCard:
        for i in range(len(self.cards)):
                if self.cards[i].number == card.number and self.cards[i].color == card.color:
                    tmp = self.cards.pop(i)
                    self.card_amount = len(self.cards)
                    return tmp
        return None
    

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
    
    def play_card(self,unocard) -> UnoCard:
        return self.cardstack.pop_card(unocard)

class Game:
    #if color or number equal...
    #user input move finished...
    #for testing console input/output...
    #two card stacks one for drawing one for field...
    #state...
    #keep track which players turn it is
    #check who is winning
    def __init__(self,player_one,player_two,main_stack):
        self.player_one = player_one
        self.player_two = player_two
        self.main_stack = main_stack

    def match_cards(self,card_1,card_2)->bool:
        pass
