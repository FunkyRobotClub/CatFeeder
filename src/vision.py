import io
import picamera
import cv2
import numpy

stream = io.BytesIO()

with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.capture(stream, format='jpeg')

buff = numpy.fromstring(stream.getvalue(), dytpe=numpy.uint8)
image = cv2.imdecode(buff, 1)

retval, dst = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

contours = cv2.findContours(dst, mode=CV_RETR_LIST, method=CV_CHAIN_APPROX_NONE)

cv2.drawContours(dst, contours, -1, (0,0,255))

cv2.imwrite('threshed.jpg', dst)
