import cv2 as cv

import config

img = cv.imread('webcam simulation.jpeg')

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(
    src=img_gray,
    thresh=config.gray_image_thresh,
    maxval=255,
    type=cv.THRESH_BINARY
)

contours, hierarchy = cv.findContours(
    image=thresh,
    mode=cv.RETR_TREE,
    method=cv.CHAIN_APPROX_NONE
)


def is_bigger_contour(contour_to_check):
    area = cv.contourArea(contour_to_check)
    return area > config.area_filter_size


bigger_contours_iterator = filter(is_bigger_contour, contours)
bigger_contours = list(bigger_contours_iterator)

for contour in contours:
    print(cv.contourArea(contour))

img_with_contours = img.copy()

cv.drawContours(
    image=img_with_contours,
    contours=bigger_contours,
    contourIdx=-1,
    color=(0, 255, 0),
    thickness=2
)

cv.imshow('contours', img_with_contours)
cv.waitKey(0)
cv.destroyAllWindows()
