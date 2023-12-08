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
    
    def __str__(self) -> str:
        return f'{str(self.color)} {str(self.number)}' 

    def match(self, other):
        return self.color == other.color or self.number == other.number
    
class CardStack:

    def __init__(self, cards: [(UnoCard, int)]):
        self.cards = cards
        self.card_amount = len(self.cards)

    def add_card(self, card: UnoCard, position: int):
        card_position = (card, position)
        self.cards.append(card_position)
        self.card_amount += 1

    def played_all_cards(self):
        return self.card_amount

    def remove_card(self, removed_card: UnoCard):
        for card in self.cards:
            unocard,_ = card
            if unocard.match(removed_card):
                self.cards.remove(card)
    
    # deprecated
    def pop_specific_card(self, card: UnoCard) -> (UnoCard, int):
        for i in range(len(self.cards)):
                if self.cards[i].number == card.number and self.cards[i].color == card.color:
                    tmp = self.cards.pop(i)
                    self.card_amount = len(self.cards)
                    return tmp
        return None
    
    # deprecated
    def get_card(self, card: UnoCard) -> (UnoCard, int):
        for i in range(len(self.cards)):
                if self.cards[i].number == card.number and self.cards[i].color == card.color:
                    return self.cards[i]
        return None
     
    def get_all_cards(self) -> [(UnoCard,int)]:
        return self.cards
    
    def cards_to_string(self) -> str:
        return ' '.join(f'{str(card)}' for card in self.get_all_cards())



