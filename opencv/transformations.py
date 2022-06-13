import cv2 as cv
import numpy as np

img = cv.imread('images/mz.jpg')


def translate(image, x, y):
    transmat = np.float32([[1, 0, x], [1, 0, y]])
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, transmat, dimensions)


#
# translated_img = translate(img, 50, 50)
# cv.imshow('translated', translated_img)

# Image rotation

def rotate(image, angle, rot_point=None):
    (width, height) = image.shape[:2]

    if rot_point is None:
        rot_point = (width // 2, height // 2)

    dimensions = (width, height)

    rot_matrix = cv.getRotationMatrix2D(rot_point, angle, 1.0)

    return cv.warpAffine(image, rot_matrix, dimensions)


rotated_image = rotate(img, 45)

cv.imshow('Rotated img', rotated_image)

cv.waitKey(0)
