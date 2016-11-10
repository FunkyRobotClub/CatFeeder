import io
import picamera
import cv2
import numpy


def take_image():
    """Returns an int representing the area of the detected contour"""
    stream = io.BytesIO()

    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.capture(stream, format='jpeg')

    buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)
    image = cv2.imdecode(buff, 1)

    retval, dst = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    mono = cv2.cvtColor(dst, cv2.cv.CV_BGR2GRAY)
    blurred = cv2.medianBlur(mono, 5)
    edge = cv2.Canny(blurred, 100, 200)
    list, hierarchy = cv2.findContours(edge, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(image, list, -1, (0,0,255))

    for c in list:
        area = cv2.contourArea(c)

    return int(area)

    # Debug, saves image of outline and area, overlayed onto original image.
    # cv2.putText(image, str(area), (100,100), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0))
    # cv2.imwrite('img.jpg', image)


def get_fill():
    """Returns percentage of bowl not white"""
    BOWL_AREA = 69
    cntrArea = take_image()
    return (cntrArea / BOWL_AREA) * 100
