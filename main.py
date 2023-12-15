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

# predict cards
init_card, position = predict_uno_cards(config.stack_camera)[0]

# for testing
# init_card = UnoCard(color=Color.BLUE, number=9)

cards = predict_uno_cards(config.robot_camera)
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