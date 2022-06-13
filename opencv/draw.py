import cv2 as cv
import numpy

blank = numpy.zeros((500, 500, 3), dtype='uint8')

# changing the color

# blank[0:300, 0:400] = 234, 234, 0

# drawing rectangle

# cv.rectangle(blank, (10, 40), (250, 250), (234, 145, 45))
# circle

# v.circle(blank, (blank.shape[0] // 2, blank.shape[1] // 2), 100, (0, 245, 124), thickness=-2)

# adding text

cv.putText(blank, "It dush valentin on openCV", (50, 255), cv.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 2)
cv.imshow("black", blank)

cv.waitKey(0)
