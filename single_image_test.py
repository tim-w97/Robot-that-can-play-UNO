import cv2 as cv

import card_cropper

dummy_img = cv.imread('dummy image.jpeg')

cropped_cards = card_cropper.crop_cards_from_img(dummy_img)

for cropped_card in cropped_cards:
    cv.imshow('cropped card', cropped_card)
    cv.waitKey()
