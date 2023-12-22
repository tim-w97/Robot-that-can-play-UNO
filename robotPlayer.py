import speaker
from control import RobotProxy
from uno_classes import UnoCard, CardStack, Color
from pyniryo import PoseObject
from player import Player
import math

"""
Calculates the poses for a specific slot.
"""
def calculate_poses(card_number: int) -> [PoseObject]:
    card_offset = 0.063
    x_start = 0.31

    if card_number < 0 or card_number > 6:
        raise "Can't pick card with index " + str(card_number)

    x_pos = x_start - card_number * card_offset

    # move above the desired card
    prepare_pose = PoseObject(
        x=x_pos,
        y=0.29,
        z=0.2,
        roll=0,
        pitch=1.57,
        yaw=0
    )

    # move a bit more down to prepare pickup
    card_pose = PoseObject(
        x=x_pos,
        y=0.29,
        z=0.15,
        roll=0,
        pitch=1.57,
        yaw=0
    )

    go_up_pose = PoseObject(
        x=x_pos,
        y=0.29,
        z=0.3,
        roll=0,
        pitch=1.57,
        yaw=0
    )

    # move the card to the stack
    stack_pose = PoseObject(
        x=0.2,
        y=-0.01,
        z=0.3,
        roll=0,
        pitch=1.57,
        yaw=0
    )

    # rotate the arm a little bit so the card falls nicely into the holder
    release_pose = PoseObject(
        x=0.2,
        y=-0.2,
        z=0.15,
        roll=1.57,
        pitch=0.9,
        yaw=-1.57
    )

    return [prepare_pose, card_pose, go_up_pose, stack_pose, release_pose]


"""
The main task of the RobotPlayer is to say what the robot has to do during the game.
At init the robotplayer has to analyze its cards
"""
class RobotPlayer(Player):

    def __init__(self, name: str, cards: [(UnoCard,int)]):
        super().__init__(name)
        self.robot = RobotProxy()
        self.stack = CardStack(cards)
        self.robot.connect()

        speaker.speak("speech/my name is rob lets play uno together.mp3")

    """
    This method has to be overwritten. Steps could be:
    1. Calculate a playable card
    2. Play the card
    3. updateStack
    """
    def handle_turn(self, activeCard: UnoCard) -> bool:
        card_position = self.get_next_card(activeCard)

        canPlay = not card_position is None

        if canPlay:
            card, position = card_position
            self.play_card(position)
            self.update_stack(card, canPlay)

        if self.card_amount == 1:
            speaker.speak("speech/uno.mp3")
        elif self.card_amount == 0:
            speaker.speak("speech/uno uno.mp3")

        return True

    """
    Returns the next playable card. If there is no card to play, it returns None instead.
    """
    def get_next_card(self, activeCard: UnoCard) -> (UnoCard, int):
        for card_position in self.stack.get_all_cards():
            card, position = card_position
            if card.match(activeCard): return card_position
        return None

    """
    Updates the stack by calculation which card has been played or drawn. 
    """
    def update_stack(self, playedCard: UnoCard, hasPlayed: bool):
        print('Stack wird geupdated')
        if hasPlayed:
            self.stack.remove_card(playedCard)

        self.card_amount = self.stack.card_amount

    """
    Moves the robot to play a card.
        1. Calculate the number of a card
        2. Calculate the poseObjects of the number
        3. Pick up the card
        4. Play the card
        5. Return to the HomePose
    """
    def play_card(self, position):
        poses: [PoseObject] = calculate_poses(position)
        self.pick_up_card(poses)
        self.robot.moveToHomePose()

    """
    The robot picks up a card.
    """
    def pick_up_card(self, poses: [PoseObject]):
        prepare, pick, go_up, stack, release = poses

        # open the grabber in case it's closed
        self.robot.release()

        # move above the desired card
        self.robot.move_pose(prepare)

        # pick down and pick the card
        self.robot.move_pose(pick)
        self.robot.grab()

        # move up again so the robot doesn't collide with the other cards
        self.robot.move_pose(go_up)

        # move to card stack
        self.robot.move_pose(stack)
        self.robot.move_pose(release)

        self.robot.release()

    """
    This method is called, after the game is finished. This method does the cleanup.
    """
    def cleanup(self):
        self.robot.disconnect()
