from . import DataLogger
from . import motor

import Site.catserver.interface.Feeder.src.timer as timer

motor.init()

while True:
    timer.sleep_remaining_time()
    motor.forward(0.01, 48)
    motor.stop()  # Saves a little power by turning off the motor coils
    DataLogger.log_data('sensor_reading')  # Will involve vision at some point

print(DataLogger.get_data())
