import cv2 as cv

video = cv.VideoCapture(0)


def rescaleFrame(frame, scale=1.5):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


while True:
    isTrue, frame = video.read()
    resized_frame = rescaleFrame(frame, 1.5)
    grayFrame = cv.cvtColor(resized_frame, cv.COLOR_BGR2GRAY)

    haar_cascade = cv.CascadeClassifier('face_detection.xml')
    face_rect = haar_cascade.detectMultiScale(grayFrame, scaleFactor=1.1, minNeighbors=6)

    for (x, y, w, h) in face_rect:
        cv.rectangle(resized_frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    cv.imshow('video', resized_frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows()
