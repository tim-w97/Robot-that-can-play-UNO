import cv2 as cv
import color_detector
import detection
import card_cropper
import config

capture = cv.VideoCapture(config.camera_index)

if not capture.isOpened():
    print('Cannot open camera. Did you set the right camera index in config.py?')
    exit()

while True:
    ret, frame = capture.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cropped_cards = card_cropper.crop_cards_from_img(frame)

    if cropped_cards is None:
        continue
    
    for cropped_card in cropped_cards:
        cv.imshow('frame', cropped_card)

        # Detect color for the card
        color = color_detector.detect_color(cropped_card)
        print('Color of this card is ' + color)

        # Detect number for the card
        number = detection.process_uno_card(cropped_card)  # Assuming cropped_card is a valid image array
        print("Number on this card is " + number)

    cv.imshow('frame', cropped_cards[0])

    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
