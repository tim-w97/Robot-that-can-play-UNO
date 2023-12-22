import config
import cv2

from uno_classes import *
from robotPlayer import RobotPlayer
from player import HumanPlayer
from game import Game

from detector import predict_uno_cards

"""
TODO:
- Analyze the initial card
- Analyze the robot's cardstack
"""

"""
# predict initial stack card
stack_cards = []

while len(stack_cards) != 1:
    stack_cards = predict_uno_cards(config.stack_camera)

    if len(stack_cards) == 0:
        input("Detected no card on the stack. Press any key to try again.")

    if len(stack_cards) > 1:
        input("Detected more than one card on the stack. Press any key to try again.")
"""


# for testing
# init_card = UnoCard(color=Color.BLUE, number=9)

cards = []

while True:
    cards = predict_uno_cards(config.robot_camera)

    if len(cards) != 7:
        input("Please ensure that the robot has 7 cards. Press any key to try again")
    else:
        break


for card, position in cards:
    print(f'Card<{card}>, position: {position}')

# init the players
robotPlayer = RobotPlayer("Rob", cards)
player = HumanPlayer("Lukas")

# run the game
game = Game(robotPlayer, player)
game.run_game()

# cleanup
cv2.destroyAllWindows()