from ultralytics import YOLO

import cv2
import config
from game_classes import *
from robotPlayer import RobotPlayer

"""
TODO:
- Analyze the initial card
- Analyze the robot's cardstack
"""

# init the model
model = YOLO(config.model_path)

# init the players
initialCard = UnoCard(3, Color.BLUE)
robotPlayer = RobotPlayer("Rob")
player = HumanPlayer("Lukas")

# run the game
game = Game(robotPlayer, player, initialCard=initialCard)
game.run_game()

# cleanup
cv2.destroyAllWindows()