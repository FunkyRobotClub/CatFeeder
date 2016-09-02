import RPi.GPIO as GPIO
import timer

AIN1 = 18
AIN2 = 23
BIN1 = 24
BIN2 = 25


def init():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(AIN1, GPIO.OUT)
    GPIO.setup(AIN2, GPIO.OUT)
    GPIO.setup(BIN1, GPIO.OUT)
    GPIO.setup(BIN2, GPIO.OUT)


def forward(delay, steps):
    for i in range(0, steps):
        setStep(1, 0, 1, 0)
        timer.sleep(delay)
        setStep(0, 1, 1, 0)
        timer.sleep(delay)
        setStep(0, 1, 0, 1)
        timer.sleep(delay)
        setStep(1, 0, 0, 1)
        timer.sleep(delay)


def backwards(delay, steps):
    for i in range(0, steps):
        setStep(1, 0, 0, 1)
        timer.sleep(delay)
        setStep(0, 1, 0, 1)
        timer.sleep(delay)
        setStep(0, 1, 1, 0)
        timer.sleep(delay)
        setStep(1, 0, 1, 0)
        timer.sleep(delay)


def stop():
    setStep(0, 0, 0, 0)


def setStep(w1, w2, w3, w4):
    GPIO.output(AIN1, w1)
    GPIO.output(AIN2, w2)
    GPIO.output(BIN1, w3)
    GPIO.output(BIN2, w4)
