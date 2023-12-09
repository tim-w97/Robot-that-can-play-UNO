from control import RobotProxy
from uno_classes import UnoCard, CardStack, Color
from pyniryo import PoseObject
from player import Player
import math

pickup_pitch = math.radians(25)
rotation_90 = math.radians(90)

x_pos_prepare = 0.12

x_pos_min = 0.2
x_pos_max = 0.35
x_pos_middle = (x_pos_min + x_pos_max) / 2

y_pos_min = -0.17
y_pos_max = 0.17

z_pos = 0.075
z_pos_up = 0.2

"""
Calculates the poses for a specific slot.
"""
def calculate_poses(card_number: int) -> [PoseObject]:
    if card_number not in range(1, 7):
        raise ValueError(f"card number {card_number} doesn't exist.")

    x_pos = x_pos_min
    y_pos = y_pos_min
    yaw = rotation_90

    if card_number > 3:
        y_pos = y_pos_max
        yaw = -rotation_90

    if card_number % 3 == 2:
        x_pos = x_pos_middle

    if card_number % 3 == 0:
        x_pos = x_pos_max
    
    prepare_pose = PoseObject(
        x=x_pos_prepare,
        y=y_pos,
        z=z_pos,
        roll=rotation_90,
        pitch=pickup_pitch,
        yaw=yaw
    )
    card_pose = PoseObject(
        x=x_pos,
        y=y_pos,
        z=z_pos,
        roll=rotation_90,
        pitch=pickup_pitch,
        yaw=yaw
    )
    stack_pose = PoseObject(
        x=-0.01,
        y=-0.2,
        z=0.14,
        roll=rotation_90,
        pitch=0.6,
        yaw=-rotation_90
    )
    return [prepare_pose, card_pose, stack_pose]


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
        self.robot.say(f"Hi my name {name}. I am glad to play with you.")

    """
    This method has to be overwritten. Steps could be:
    1. Calculate a playable card
    2. Play the card
    3. updateStack
    """
    def handle_turn(self, activeCard: UnoCard) -> bool:
        card_position = self.get_next_card(activeCard)
        card, position = card_position
    
        canPlay = not card_position is None
        if canPlay:
            self.play_card(position)
        self.update_stack(card, canPlay)

        if self.card_amount == 1:
            self.robot.say("Uno")
        elif self.card_amount == 0:
            self.robot.say("Uno Uno")

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
        prepare, pick, stack = poses
        # open the grabber in case it's closed
        self.robot.release()

        # pick up card with given card_number
        self.robot.move_pose(prepare)

        # move card up
        self.robot.move_pose(pick)
        self.robot.grab()

        # move to home pose, but little bit higher
        self.robot.moveJoints(0, 0.5, -0.7, 0, 0, 0)

        # move to card stack
        self.robot.move_pose(stack)
        self.robot.release()

    """
    This method is called, after the game is finished. This method does the cleanup.
    """
    def cleanup(self):
        self.robot.disconnect()