from uno_classes import UnoCard
from detector import predict_uno_cards

import config

from time import sleep
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
    Handles the turn of the player. The player play a card or tells the system that he can't play.
    """
    def handle_turn(self, activeCard: UnoCard) -> bool:
        # every second the models take a picture and scan the card_stack for a new card
        # if the player is not able to draw a card signals the system by typing in
        # self.card_amount = int(input(f"It's your turn {self.name}. How many cards do you have?"))
        card, position = predict_uno_cards(config.stack_camera)[0]
        delay = config.play_time
        while delay > 0 and card.match_exactly(activeCard):
            sleep(1)
            delay -= 1
            card, position = predict_uno_cards(config.stack_camera)[0]

    def cleanup(self):
        return True