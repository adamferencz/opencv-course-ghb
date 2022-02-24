import cv2 as cv
import sys
import numpy as np

capture = cv.VideoCapture(0)

isTrue, frame = capture.read()
blank = np.zeros((frame.shape[0], frame.shape[1]), dtype='uint8')
while True:
    isTrue, frame = capture.read()

    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    low_color = np.array([161, 155, 84])
    high_color = np.array([179, 255, 255])
    mask = cv.inRange(hsv_frame, low_color, high_color)

    # Eroding
    eroded = cv.erode(mask, (8,8), iterations=5)

    # Dilating the image
    dilated = cv.dilate(eroded, (3,3), iterations=5)
    print("dilated", dilated)
    

    print("blank", blank)
    blank = cv.bitwise_or(blank, dilated)
    

    cv.imshow('hsv_man', frame)
    cv.imshow('mask', mask)
    cv.imshow('Eroded', eroded)
    cv.imshow('Dilated', dilated)
    cv.imshow('result', blank)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()