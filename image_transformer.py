import cv2
import numpy as np
import config


# transform the image so the yolo model has a better chance of detecting the cards
def transform_image(image):
    height, width, channels = image.shape

    src_points = [
        [config.trapeze_margin, 0],
        [0, height],
        [width, height],
        [width - config.trapeze_margin, 0]
    ]

    dst_points = [
        [0, 0],
        [0, height],
        [width, height],
        [width, 0]
    ]

    matrix = cv2.getPerspectiveTransform(
        np.float32(src_points),
        np.float32(dst_points)
    )

    transformed_image = cv2.warpPerspective(image, matrix, (width, height))
    resized_image = cv2.resize(transformed_image, (int(width * config.resize_factor), height))
    rotated_image = cv2.rotate(resized_image, cv2.ROTATE_90_CLOCKWISE)

    return rotated_image
