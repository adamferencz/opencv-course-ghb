import cv2 as cv
import sys

#img = cv.imread("cats_2.jpg")

#cv.imshow("Cat", img)

capture = cv.VideoCapture("Videos/kitten.mp4")

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()