import timer
import motor

while True:
    timer.sleepRemainingTime()
    motor.forward(0.01, 48)
