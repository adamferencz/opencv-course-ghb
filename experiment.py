import cv2 as cv
import sys
import numpy as np

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    greencat = np.copy(frame)
    greencat[:, :, 0] = 0
    greencat[:, :, 2] = 0

    greencat2 = cv.GaussianBlur(greencat,(5, 5), cv.BORDER_DEFAULT)
    supercat = np.uint8((frame + greencat2)/2)-50

    cv.imshow('Video', supercat)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()