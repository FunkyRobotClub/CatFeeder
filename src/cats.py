from . import timer
from . import motor
from . import DataLogger
from . import vision

motor.init()

while True:
    timer.sleep_remaining_time()
    DataLogger.log_data(vision.get_fill())
    motor.forward(0.1, 12)    # 12 steps / revolution
    motor.stop()  # Saves a little power by turning off the motor coils
