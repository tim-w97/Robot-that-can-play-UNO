import cv2 as cv
import detector

dummy_img = cv.imread('dummy image.jpeg')

contours = detector.get_contours(dummy_img)

# Find bounding box and extract ROI
for c in contours:
    x,y,w,h = cv.boundingRect(c)
    ROI = dummy_img[y:y+h, x:x+w]
    break

cv.imshow('ROI',ROI)

cv.waitKey()