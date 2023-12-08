from ultralytics import YOLO
from image_transformer import transform_image
from color_detector import determine_color
from game_classes import UnoCard

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
def predict_uno_cards(camera_index = config.robot_camera):
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

    # if it's the robot cam, we need to change the perspective so the uno card detection works better
    if camera_index == config.robot_camera:
        transformed_image = transform_image(frame)
    else:
        transformed_image = frame

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

        predicted_uno_cards.append((uno_card, (bounding_box[0], bounding_box[1])))

    return sort(predicted_uno_cards)

def sort(results: [(UnoCard, (float,float))]) -> [(UnoCard, int)]:
    # 1. remove duplicates
    results = remove_duplicates(results)

    # 2. sortiere nach y
    length = len(results)
    for i in range(0, length):
        smallestIdx = i
        for j in range(i + 1, length):
            _, (s_x,s_y) = results[smallestIdx]
            _, (r_x, r_y) = results[j]
            if r_y < s_y:
                smallestIdx = j
        tmp = results[smallestIdx]
        results[smallestIdx] = results[i]
        results[i] = tmp

    # 3. sortiere alle karten nach x
    for i in range(0, 3):
        smallestIdx = i
        for j in range(i + 1, 3):
            _, (s_x,s_y) = results[smallestIdx]
            _, (r_x, r_y) = results[j]
            if r_x < s_x:
                smallestIdx = j     
        tmp = results[smallestIdx]
        results[smallestIdx] = results[i]
        results[i] = tmp  

    for i in range(3, 6):
        smallestIdx = i
        for j in range(i + 1, 6):
            _, (s_x,s_y) = results[smallestIdx]
            _, (r_x, r_y) = results[j]
            if r_x < s_x:
                smallestIdx = j     
        tmp = results[smallestIdx]
        results[smallestIdx] = results[i]
        results[i] = tmp  

    for card, (x, y) in results:
        print(f'Card<{card}>, x: {x}, y: {y}')

    # 3. transform cards
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