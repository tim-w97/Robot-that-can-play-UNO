from control import RobotProxy
from ./game_classes import CardStack

"""
The main task of the RobotPlayer is to say what the robot has to do during the game.
At init the robotplayer has to analyze its cards
"""
class RobotPlayer:
    def __init__(self):
        self.robot = RobotProxy()
        self.robot.connect()

        self.stack = CardStack([])
        self.updateStacks()
        

    """
    This method detects both card stacks and updates the robot's attributes.
    Here is the color and number detection needed.
    """
    def updateStacks(self):
        pass

    """
    Moves the robot to play a card.
    """
    def playCard(self, card):
        pass

    