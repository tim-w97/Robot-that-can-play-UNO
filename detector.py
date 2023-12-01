from ultralytics import YOLO
from image_transformer import transform_image
from color_detector import determine_color
from game_classes import UnoCard

import cv2
import config
import numpy

"""
This methods predicts all uno cards from the given image

1. Transform the given image so the number detection works better
2. Predict all uno cards and their corresponding positions (1-6)
3. Return an array of tuples (Uno Card, Position)
"""
def predict_uno_cards(image):
    predicted_uno_cards = []

    # ignore this code (start)
    # but leave it here so the color detector works
    def patch(a):
        return a.item()

    setattr(numpy, "asscalar", patch)

    # ignore this code (end)

    # Load a model and the card numbers (classes)
    model = YOLO(config.model_path)
    card_numbers = model.names

    transformed_image = transform_image(image)

    # predict all uno cards from the image
    results = model(transformed_image)

    if len(results) == 0:
        return []

    first_result = results[0]

    for box in first_result.boxes:
        # get the predicted card number
        predicted_class = int(box.cls)
        card_number = card_numbers[predicted_class]

        # get coordinates of the bounding box
        # xyxy means x1 and y1 of the top left corner and x2 and y2 of the bottom right corner
        bounding_boxes = box.xyxy.tolist()

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
        uno_card = UnoCard(card_number, color)
        predicted_uno_cards.append(uno_card)

    return predicted_uno_cards


# test the method
cards = predict_uno_cards(
    image=cv2.imread('uno cards test image.jpeg')
)

for card in cards:
    print(card)
