from control import RobotProxy
from ./game_classes import UnoCard, CardStack, Player
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
    def handle_turn(self) -> bool:
        card = self.get_next_card()
        if card is None:
            return False

        self.play_card(card)
        self.update_stack()
        return True

    """
    Returns the next playable card. If there is no card to play, it returns None instead.
    """
    def get_next_card(self) -> UnoCard:
        self.card

    def update_stack(self):
        pass

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
        #TODO
        pass

    """
    This method is called, after the game is finished. This method does the cleanup.
    """
    def finish(self):
        self.robot.disconnect()