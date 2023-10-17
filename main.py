import cv2 as cv
import detector
import config

capture = cv.VideoCapture(config.camera_index)

if not capture.isOpened():
    print('Cannot open camera')
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = capture.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # operations on the frame belong here

    img_with_contours = detector.detect_contours(frame)

    cv.imshow('frame', img_with_contours)

    # press q to quit
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
capture.release()
cv.destroyAllWindows()
