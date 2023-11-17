from control import RobotProxy
from ./game_classes import CardStack, Player
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
        self.updateStack()

    """
    This method has been overwritten.
    """
    def handleTurn(self) -> bool:
        pass

    def updateStack(self):
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
    def playCard(self, card):
        pose = calculatePose(card)
        self.robot.move(Poses.CARD_STACK)
        self.robot.grab()
        self.robot.move(Poses.HOME)

        self.robot.move(POSES.MAIN_STACK)
        self.robot.release()
        self.robot.move(Poses.HOME)

    """
    Calculates the pose for the specific uno card.
    """
    def calculatePose(self, card):
        #TODO
        pass

    """
    This method is called, after the game is finished. This method does the cleanup.
    """
    def finish(self):
        self.robot.disconnect()