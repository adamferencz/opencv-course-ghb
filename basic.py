import cv2 as cv
import numpy as np

img = cv.imread("Photos/cat.jpg")
cv.imshow("Ca1", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Ca2", gray)

greencat = np.copy(img)
greencat[:, :, 0] = 0
greencat[:, :, 2] = 0
# cv.imshow("Ca3", greencat)

greencat2 = cv.GaussianBlur(greencat,(5, 5), cv.BORDER_DEFAULT)
cv.imshow("Ca4", greencat2)
cv.imshow("Ca1", img)
supercat = np.uint8((img + greencat2)/2)-50
cv.imshow("Ca5", supercat)


supercat2 = cv.addWeighted(img, 0.5, greencat2, 0.5, 0.0)
cv.imshow("Ca6", supercat2)

# Edge Cascade
man = cv.imread("Photos/man.jpg")
def rescale(frame, scale=0.75):
    width = frame.shape[1] * scale
    height = frame.shape[0] * scale

    dimensions = (int(width), int(height))

    new_frame = cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    return new_frame

man = rescale(man, 0.3)
canny = cv.Canny(man, 400, 500)
cv.imshow('Canny Edges', canny)


# Eroding
eroded = cv.erode(canny, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Dilating the image
dilated = cv.dilate(eroded, (3,3), iterations=5)
cv.imshow('Dilated', dilated)

hsv_man = cv.cvtColor(man, cv.COLOR_BGR2HSV)

low_color = np.array([150, 15, 70])
high_color = np.array([210, 255, 255])
mask = cv.inRange(hsv_man, low_color, high_color)

cv.imshow('hsv_man', hsv_man)
cv.imshow('mask', mask)

cv.waitKey(0)