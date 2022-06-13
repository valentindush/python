import cv2 as cv

img = cv.imread("images/mz.jpg")

# Gray scale
grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# using blur effects

blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)

#Finding edges in image using cv.canny

canny = cv.Canny(img, 127, 175)

cv.imshow('Edges', canny)

cv.waitKey(0)
