from datetime import datetime as dt
import time

checkTime = True
while checkTime:
    sysTime = str(dt.time(dt.now()))[:8]
    time.sleep(60)
    print(sysTime)
