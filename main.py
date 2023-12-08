from ultralytics import YOLO

import cv2
import config
from game_classes import *
from robotPlayer import RobotPlayer

from detector import predict_uno_cards

"""
TODO:
- Analyze the initial card
- Analyze the robot's cardstack
"""

# predict cards
initialCard = predict_uno_cards(config.stack_camera)
cards = predict_uno_cards(config.robot_camera)

# init the players
robotPlayer = RobotPlayer("Rob", cards)
player = HumanPlayer("Lukas")

# run the game
game = Game(robotPlayer, player, initialCard=initialCard)
game.run_game()

# cleanup
cv2.destroyAllWindows()