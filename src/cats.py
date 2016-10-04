import src.timer as timer
import src.motor as motor

motor.init()

while True:
    timer.sleepRemainingTime()
    motor.forward(0.01, 48)
    motor.stop()  # Saves a little power by turning off the motor coils
