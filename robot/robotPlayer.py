from control import RobotProxy
from game_classes import UnoCard, CardStack, Player
from poses import Poses

"""
The main task of the RobotPlayer is to say what the robot has to do during the game.
At init the robotplayer has to analyze its cards
"""
class RobotPlayer(Player):

    def __init__(self, name: str):
        self.robot = RobotProxy()
        self.robot.connect()

        self.stack = CardStack([])
        self.update_stack()

    """
    This method has to be overwritten. Steps could be:
    1. Calculate a playable card
    2. Play the card
    3. updateStack
    """
    def handle_turn(self, activeCard: UnoCard) -> bool:
        card = self.get_next_card()
        canPlay = card is None
        if canPlay:
            self.play_card(card)
        else:
            # TODO: Later on, draw a card
            pass
        self.update_stack(card, canPlay)
        return True

    """
    Returns the next playable card. If there is no card to play, it returns None instead.
    """
    def get_next_card(self, activeCard: UnoCard) -> UnoCard:
        for card in self.stack.get_all_cards():
            if card.match(activeCard): return card
        return None

    """
    Updates the stack by calculation which card has been played or drawn. 
    Later on, we can add camera detection here.
    """
    def update_stack(self, playedCard: UnoCard, hasPlayed: bool):
        if hasPlayed:
            self.stack.remove_card(playedCard)
        else:
            self.stack.add_card(playedCard)

    """
    Moves the robot to play a card.
        1. Calculate the position of the playable card
        2. Move to the card
        3. Grab the card
        4. Move to HomePose to prevent damage
        5. Move to pose of the main deck
        6. Release the card
        7. Move to HomePose again
    """
    def play_card(self, card: UnoCard):
        pose = calculate_pose(card)
        self.robot.move(Poses.CARD_STACK)
        self.robot.grab()
        self.robot.move(Poses.HOME)

        self.robot.move(POSES.MAIN_STACK)
        self.robot.release()
        self.robot.move(Poses.HOME)

    """
    Calculates the pose for the specific uno card.
    """
    def calculate_pose(self, card: UnoCard):
        #TODO: Add camera detection here to localize the position of the specific card.
        pass

    """
    This method is called, after the game is finished. This method does the cleanup.
    """
    def cleanup(self):
        self.robot.disconnect()