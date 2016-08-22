from datetime import datetime as dt
import time

import motor

turnTimes = ["9:00:00", "17:00:00"]

checkTime = True
while checkTime:
    sysTime = str(dt.time(dt.now()))[:8]
    if sysTime in turnTimes:
        motor.forward(0.1, 12)
    time.sleep(60)
    print(sysTime)
