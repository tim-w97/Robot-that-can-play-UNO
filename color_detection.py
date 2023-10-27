import cv2
import numpy as np
from PIL import Image


def color_detection(filename):
    image = cv2.imread(filename)

    # Get the size (width and height) of the image
    height, width, channels = image.shape

    # Crop the card region
    # You'll need to define the coordinates for cropping
    card = image[0:height, 0:width]

    # Convert to HSV color space
    hsv = cv2.cvtColor(card, cv2.COLOR_BGR2HSV)

    # Define color ranges for Uno card colors
    color_ranges = {
        "red": ([0, 100, 100], [10, 255, 255]),
        "blue": ([100, 100, 100], [130, 255, 255]),
        "green": ([40, 100, 100], [80, 255, 255]),
        "yellow": ([20, 100, 100], [35, 255, 255]),
    }

    # Check which color range the card falls into
    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(hsv, lower, upper)
        if mask.sum() > 10:  # You may need to adjust the threshold
            print("Detected Uno card color:", color)
            return color

    return "not recognized"
