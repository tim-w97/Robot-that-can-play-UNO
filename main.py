import cv2 as cv
import color_detector
import card_cropper
import detector
import config

capture = cv.VideoCapture(config.camera_index)

#print("color is: ", color_detection.color_detection("color_test_images/green.jpg"))
if not capture.isOpened():
    print('Cannot open camera. Did you set the right camera index in config.py?')
    exit()

# TODO: This could lead to performance issues, set a fps limit
while True:
    # Capture frame-by-frame
    ret, frame = capture.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # operations on the frame belong here

    cropped_cards = card_cropper.crop_cards_from_img(frame)

    if cropped_cards is None:
        continue

    cv.imshow('frame', cropped_cards[0])

    # press q to quit
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
capture.release()
cv.destroyAllWindows()
