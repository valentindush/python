import cv2 as cv
from cv2 import imshow

# img = cv.imread("images/mz.jpg")

# cv.imshow("cat", img)

#Reading videos

def rescaleFrame(frame, scale=1.5):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    frameResized = rescaleFrame(frame)
    cv.imshow("video", frameResized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows()