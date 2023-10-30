import cv2 as cv
import detector
import numpy as np


def crop_cards_from_img(img):
    contours = detector.get_contours(img)

    if len(contours) == 0:
        return None

    cropped_cards = []

    for contour in contours:
        rect = cv.minAreaRect(contour)

        box = cv.boxPoints(rect)
        box = np.intp(box)

        width = int(rect[1][0])
        height = int(rect[1][1])

        src_pts = box.astype("float32")

        # coordinate of the points in box points after the rectangle has been
        # straightened
        dst_pts = np.array(
            object=[
                [0, height-1],
                [0, 0],
                [width-1, 0],
                [width-1, height-1]
            ],
            dtype="float32"
        )

        # the perspective transformation matrix
        m = cv.getPerspectiveTransform(src_pts, dst_pts)

        # directly warp the rotated rectangle to get the straightened rectangle
        warped_img = cv.warpPerspective(img, m, (width, height))

        height, width, channels = warped_img.shape

        if width > height:
            warped_img = cv.rotate(warped_img, cv.ROTATE_90_CLOCKWISE)

        cropped_cards.append(warped_img)

    return cropped_cards
