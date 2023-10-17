import numpy as np
import cv2 as cv

img = cv.imread('webcam simulation.jpeg')

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(
    src=img_gray,
    thresh=130,
    maxval=255,
    type=cv.THRESH_BINARY
)

cv.imshow('thresh', thresh)
cv.waitKey(0)

contours, hierarchy = cv.findContours(
    image=thresh,
    mode=cv.RETR_TREE,
    method=cv.CHAIN_APPROX_NONE
)

img_with_contours = img.copy()

cv.drawContours(
    image=img_with_contours,
    contours=contours,
    contourIdx=-1,
    color=(0,255,0),
    thickness=2
)

cv.imshow('contours', img_with_contours)
cv.waitKey(0)
cv.destroyAllWindows()