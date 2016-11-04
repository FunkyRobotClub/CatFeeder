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

cv2.imwrite('threshed.jpg', dst)