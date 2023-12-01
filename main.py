from ultralytics import YOLO
from image_transformer import transform_image
from color_detector import determine_color

import cv2
import config
from game_classes import *
from robotPlayer import RobotPlayer

import numpy


"""
TODO:
- Import the model
- Init the RobotPlayer
- Init the HumanPlayer
- Analyze the initCard
- Create the game instance
- Run the game
"""

# init the model
model = YOLO(config.model_path)

# init the player
initialCard = UnoCard(3, Color.BLUE)
robotPlayer = RobotPlayer("Rob", model)
player = HumanPlayer("Lukas")

# run the game
game = Game(robotPlayer, player, initialCard=initialCard)
game.run_game()

# cleanup
cv2.destroyAllWindows()

def getInitCard() -> UnoCard:
    cap = cv2.VideoCapture(config.camera_index)
    ret, image = cap.read()

    transformed_image = transform_image(image)
    results = model(transformed_image)

    if len(results) > 0:
        first_result = results[0]

        plot = first_result.plot()

        for box in first_result.boxes:
            # get coordinates of the bounding box
            # xyxy means x1 and y1 of the top left corner and x2 and y2 of the bottom right corner
            bounding_boxes = box.xyxy.tolist()

            # determine the position of the pixel on the center right of the bounding box

            if len(bounding_boxes) == 0:
                continue

            bounding_box = bounding_boxes[0]

            center_right = (
                int(bounding_box[2]),
                int((bounding_box[1] + bounding_box[3]) / 2)
            )

            color_bgr = transformed_image[
                center_right[1],
                center_right[0]
            ]

            color = determine_color(color_bgr)

            cv2.putText(
                plot,
                color.name,
                center_right,
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2
            )

        cv2.imshow('Detected Uno Cards', plot)
    else:
        cv2.imshow('No Objects', transformed_image)

    cap.release()

