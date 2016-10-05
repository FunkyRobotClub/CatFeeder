from datetime import datetime as dt
import time

sysTime = ""
turnTimes = ["09:00:00", "15:10:00"]


def set_time():
    global sysTime
    sysTime = str(dt.time(dt.now()))[:8]


def get_date():
    set_time()
    return str(dt.date(dt.now()))


def to_seconds(hms):
    # Turns HH:MM:SS into seconds
    s = hms.split(':')
    return (int(s[0])*3600)+(int(s[1])*60)+(int(s[2]))


def next_alarm():
    global sysTime
    smallest = 86400
    for turnTime in turnTimes:
        if to_seconds(turnTime) < to_seconds(sysTime):
            print(turnTime + " has already passed")
        elif to_seconds(turnTime) < smallest:
            smallest = to_seconds(turnTime)
    if smallest == 86400:
        return smallest + to_seconds(turnTimes[0])
    else:
        return smallest


def sleep_remaining_time():
    set_time()
    global sysTime
    print("Waiting for " + str(next_alarm() - to_seconds(sysTime)) + " seconds")
    time.sleep(next_alarm() - to_seconds(sysTime))
    print("Done!")
