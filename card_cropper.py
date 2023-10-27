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

rect = cv.minAreaRect(contours[1])

box = cv.boxPoints(rect)
box = np.intp(box)

cv.drawContours(
    dummy_img,
    [box],
    0,
    (0, 0, 255),
    2
)

cv.imshow('cropped card',dummy_img)
cv.waitKey()