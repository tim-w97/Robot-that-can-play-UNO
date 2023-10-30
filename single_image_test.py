import cv2 as cv

import card_cropper
import color_detector

dummy_img = cv.imread('dummy image.jpeg')

cropped_cards = card_cropper.crop_cards_from_img(dummy_img)

for cropped_card in cropped_cards:
    cv.imshow('cropped card', cropped_card)

    color = color_detector.detect_color(
        card_img=cropped_card
    )

    print('Color of this card is ' + color)

    cv.waitKey()
