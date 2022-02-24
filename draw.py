import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)
print(blank)

#       x    y      B   G   R
blank[0:50, 0:50] = 0, 255, 0
cv.imshow('Blank2', blank)
print(blank)

# Reading an image in default mode
image = blank

# Using cv2.rectangle() method
# Draw a rectangle with blue line borders of thickness of 2 px
image = cv.rectangle(image, (5, 5), (220, 220), (255, 0, 0), -1)
  
# Displaying the image 
cv.imshow('Image22', image) 

# 3. Draw A circle
image = cv.circle(blank, (250, 250), 40, (0,0,255),-1)
cv.imshow('Circle', blank)

# 4. Draw a line
image = cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

cv.putText(image, 'Heeehooooo..', (300, 100), cv.FONT_HERSHEY_TRIPLEX, 5.0, (0, 255, 0), 1)
cv.imshow('Line', blank)
cv.waitKey(0)