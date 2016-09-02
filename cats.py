import timer
import motor

motor.init()

while True:
    timer.sleepRemainingTime()
    motor.forward(0.01, 48)
