from . import timer
from . import motor

motor.init()

while True:
    timer.sleep_remaining_time()
    motor.forward(0.1, 12)    # 12 steps / revolution
    motor.stop()  # Saves a little power by turning off the motor coils
    # DataLogger.log_data(sensor_reading)   Will involve vision at some point
