import config
import cv2

from uno_classes import *
from robotPlayer import RobotPlayer
from player import HumanPlayer
from game import Game

from detector import predict_uno_cards

# Detect the CardStack
cards = predict_uno_cards(config.robot_camera)

# A quick print
for card, position in cards:
    print(f'Card<{card}>, position: {position}')

# Init of the players
robotPlayer = RobotPlayer("Rob", cards)
player = HumanPlayer("Lukas")

# Run the game
game = Game(robotPlayer, player)
game.run_game()

# Cleanup
cv2.destroyAllWindows()