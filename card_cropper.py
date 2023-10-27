import cv2 as cv
import detector
import numpy as np

dummy_img = cv.imread('dummy image.jpeg')

contours = detector.get_contours(dummy_img)

# Find bounding box and extract ROI
for c in contours:
    x,y,w,h = cv.boundingRect(c)
    ROI = dummy_img[y:y+h, x:x+w]
    break

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
M = cv.getPerspectiveTransform(src_pts, dst_pts)

# directly warp the rotated rectangle to get the straightened rectangle
warped = cv.warpPerspective(dummy_img, M, (width, height))

cv.imshow('warped card', warped)
cv.waitKey()