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

class Player:

    def __init__(self,name,cards):
        self.player = name
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


def test_func():
    cards = [UnoCard(1,Color.RED),UnoCard(7,Color.GREEN),UnoCard(5,Color.BLUE)]
    p1 = Player("John doe",cards)
    p1.add_card(UnoCard(2,Color.YELLOW))
    p1.remove_card(UnoCard(2,Color.YELLOW))
    print(p1.card_amount)

test_func()

