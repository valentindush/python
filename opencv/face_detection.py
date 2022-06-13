import cv2 as cv


def resize_image(frame, scale=1.5):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('images/group.jpg')
image2 = resize_image(img, 0.25)
grayImage = cv.cvtColor(image2, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('face_detection.xml')

faces_rect = haar_cascade.detectMultiScale(grayImage, scaleFactor=1.1, minNeighbors=6)

for (x, y, w, h) in faces_rect:
    cv.rectangle(image2, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow('Detected face', image2)
print(f'Number of faces = {len(faces_rect)}')

cv.waitKey(0)
