from uno_classes import UnoCard
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