import cv2 as cv
import detector
import numpy as np


def crop_card_from_img(img):
    contours = detector.get_contours(img)

    if len(contours) == 0:
        return None

    rect = cv.minAreaRect(contours[0])

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

    return warped_img
