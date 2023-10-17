import cv2 as cv

capture = cv.VideoCapture(0)

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

    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', gray_img)

    # press q to quit
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
capture.release()
cv.destroyAllWindows()
