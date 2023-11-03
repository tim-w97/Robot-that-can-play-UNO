import cv2
import numpy as np
import game_classes as gc
from PIL import Image


def detect_color(card_img):
    # Get the size (width and height) of the image
    height, width, channels = card_img.shape

    # Crop the card region
    # You'll need to define the coordinates for cropping
    card = card_img[0:height, 0:width]

    # Convert to HSV color space
    hsv = cv2.cvtColor(card, cv2.COLOR_BGR2HSV)

    # Define color ranges for Uno card colors
    color_ranges = {
        gc.Color.RED: ([0, 100, 100], [10, 255, 255]),
        gc.Color.BLUE: ([100, 100, 100], [130, 255, 255]),
        gc.Color.GREEN: ([40, 100, 100], [80, 255, 255]),
        gc.Color.YELLOW: ([20, 100, 100], [35, 255, 255]),
    }

    # Check which color range the card falls into
    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(hsv, lower, upper)
        if mask.sum() > 10:  # You may need to adjust the threshold
            return color

    return "not recognized"
