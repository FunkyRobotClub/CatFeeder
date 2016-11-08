import io
import picamera
import cv2
import numpy

stream = io.BytesIO()

with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.capture(stream, format='jpeg')

buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)
image = cv2.imdecode(buff, 1)

retval, dst = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
mono = cv2.cvtColor(dst, cv2.cv.CV_BGR2GRAY)
cv2.imwrite('threshed.jpg', mono)
blurred = cv2.medianBlur(mono, 5)
edge = cv2.Canny(blurred, 100, 200)
list, array = cv2.findContours(edge, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)

cv2.imwrite('img1.jpg', mono)

cv2.drawContours(image, list, -1, (0,0,255))

cv2.imwrite('img2.jpg', mono)

