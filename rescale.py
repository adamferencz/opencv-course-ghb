import cv2 as cv
import sys

img = cv.imread("Photos/cat_large.jpg")
print(img.shape)

cv.imshow("Cat", img)

def rescale(frame, scale=0.75):
    width = frame.shape[1] * scale
    height = frame.shape[0] * scale

    dimensions = (int(width), int(height))

    new_frame = cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    return new_frame

new_img = rescale(img, 0.2)
print(new_img.shape)
cv.imshow("Catnew", new_img)

cv.waitKey(0)