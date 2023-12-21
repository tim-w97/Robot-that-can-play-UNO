from ultralytics import YOLO
from color_detector import determine_color
from uno_classes import UnoCard, Color

import cv2
import config
import numpy

"""
This methods predicts all uno cards from the given image

1. Capture a image from the given camera
2. If it's the robot camera, transform the image so the number detection works better
3. Predict all uno cards and their corresponding positions (1-6)
4. Return an array of tuples (Uno Card, Position)
"""
def predict_uno_cards(camera_index = config.robot_camera) -> [(UnoCard, int)]:
    # TODO: Kameraindex angeben
    predicted_uno_cards = []

    # ignore this code (start)
    # but leave it here so the color detector works
    def patch(a):
        return a.item()

    setattr(numpy, "asscalar", patch)

    # ignore this code (end)

    # capture the image
    camera = cv2.VideoCapture(camera_index)

    ret, frame = camera.read()

    if not ret:
        print("Failed to capture the image!")
        return []

    # Load a model and the card numbers (classes)
    model = YOLO(config.model_path)
    card_numbers = model.names

    # predict all uno cards from the image
    results = model(frame)

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

        color_bgr = frame[
            center_right[1],
            center_right[0]
        ]

        color = determine_color(color_bgr)
        uno_card = UnoCard(card_number, color)

        predicted_uno_cards.append((uno_card, (bounding_box[0], bounding_box[1])))

    if camera_index == config.stack_camera:
        return predicted_uno_cards

        # for testing
        # return [(UnoCard(color=Color.BLUE, number=9), 2)]

    return map_to_position(predicted_uno_cards)


def map_to_position(results: [(UnoCard, (float,float))]) -> [(UnoCard, int)]:
    # remove duplicates
    results = remove_duplicates(results)

    # transform cards
    sol = calculate_positions(results)

    return sol

def remove_duplicates(entries: [(UnoCard, (float, float))], allowance = 5) -> [(UnoCard, (float, float))]:
    # 1. map all 
    # 2. check in every insertion if entry already exists
    sol = []
    for entry in entries:
        card, (x, y) = entry
        exists = False
        for s in sol:
            card_s, (s_x, s_y) = s
            if abs(s_y - y) <= allowance and abs(s_x - x) <= allowance:
                exists = True
                break
        if not exists:
            sol.append(entry)
    return sol

def calculate_positions(entries: [(UnoCard, (float, float))]) -> [(UnoCard, int)]:
    idx = 3
    sol = []
    for r in entries:
        card, boundings = r
        sol.append((card, idx))
        idx -= 1
        if idx == 0:
            idx = 6
    return sol

# test the method
# cards = predict_uno_cards(
#     image=cv2.imread('uno cards test image.jpeg')
# )
# for card, position in cards:
#     print(card, position)