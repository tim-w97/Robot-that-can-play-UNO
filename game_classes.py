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

"""
This class represents a player. The game does not distinguish between a human and a robot.
A Human Player has to type in the number of his cards. He doesn't need a virtual card deck.
A robot need a virtual card stack and a physical one. He has to do some further steps.
"""
class Player:

    def __init__(self, name: str):
        self.name = name
        self.card_amount = 6

    """
    This method returns the current amount of cards
    """
    def get_card_count(self) -> int:
        return self.card_amount
    
    """
    This method is called from the game and needs to be overwritten.
    """
    def handle_turn(self, activeCard: UnoCard) -> bool:
        pass

    def cleanup(self):
        pass

    def __str__(self) -> str:
        return self.name

class HumanPlayer(Player):
    def __init__(self, name: str):
        super(HumanPlayer, self).__init__(name)

    """
    Waits on the player to type in the number of cards he has.
    """
    def handle_turn(self, activeCard: UnoCard) -> bool:
        self.card_amount = int(input(f"It's your turn {self.name}. How many cards do you have?"))

    def cleanup(self):
        return True


"""
This is the class to control the game. It is responsible for a game flow.
How to use Game:
1. Create an initial unocard
2. Create an instance
3. Call run_game
"""
class Game:

    def __init__(self, *args: [Player], initialCard: UnoCard):
        if len(args) < 2: raise Exception("You need at least two players!")
        self.players = args
        self.activePlayer = -1
        self.activeCard = initialCard

        # only for testing
        self.cards = [
            UnoCard(3, Color.BLUE),
            UnoCard(2, Color.BLUE),
            UnoCard(2, Color.GREEN),
            UnoCard(4, Color.GREEN),
            UnoCard(4, Color.RED),
            UnoCard(5, Color.RED),
            UnoCard(5, Color.YELLOW),
            UnoCard(8, Color.YELLOW),
            UnoCard(9, Color.YELLOW),
            UnoCard(9, Color.BLUE),
            UnoCard(6, Color.BLUE),
            UnoCard(1, Color.BLUE)
        ]
        self.card_idx = 0

    def get_next_player(self) -> Player:
        if self.activePlayer == len(self.players) - 1:
            self.activePlayer = 0
        else:
            self.activePlayer += 1
        return self.players[self.activePlayer]
    
    def is_active_player_winning(self) -> bool:
        if self.activePlayer == -1: return False

        player = self.players[self.activePlayer]

        return player.get_card_count() == 0

    """
    This method analyze the main deck by card detection.
    Detect the active card.
    """
    def update_game_stats(self):
        # TODO: Update the stack and analyze the activeCard
        
        self.activeCard = self.cards[self.card_idx]
        self.card_idx += 1
        print(str(self.activeCard))

    """
    This is the main method to call.
    """
    def run_game(self):
        self.update_game_stats()
        while not self.is_active_player_winning():
            player = self.get_next_player()
            player.handle_turn(self.activeCard)
            self.update_game_stats()
        print(f"Congrats. {player} won the game.")

        # Cleanup
        for player in self.players:
            player.cleanup()
