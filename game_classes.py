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
    
    def pop_specific_card(self,card) -> UnoCard:
        try:
            for i in range(len(self.cards)):
                    if self.cards[i].number == card.number and self.cards[i].color == card.color:
                        tmp = self.cards.pop(i)
                        self.card_amount = len(self.cards)
                        return tmp
        except TypeError:
            print("You dont have this card in your deck")
            # try again?
            # pull card
    
    def get_card(self,card) -> UnoCard:
        try:
            for i in range(len(self.cards)):
                    if self.cards[i].number == card.number and self.cards[i].color == card.color:
                        return self.cards[i]
        except TypeError:
            print("You dont have this card in your deck")
            # try again?

    

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
    
    def get_card(self,unocard) -> UnoCard:
        return self.cardstack.get_card(unocard)
    
    #Removes and returns a specific card from the stack
    def play_card(self,unocard) -> UnoCard:
        return self.cardstack.pop_specific_card(unocard)

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
        if(card_1.color == card_2.color or card_1.number == card_2.number):
            return True
        return False
    
    def set_winner(self,player):
        if player.get_card_count() == 0:
            print(f'{player.name} has won the game!')
            self.game_is_over = True
        else:
            self.game_is_over = False
