from datetime import datetime as dt
import time

sysTime = ""
turnTimes = ["09:00:00", "15:10:00"]


def setTime():
    global sysTime
    sysTime = str(dt.time(dt.now()))[:8]


def toSeconds(hms):
    # Turns HH:MM:SS into seconds
    s = hms.split(':')
    return (int(s[0])*3600)+(int(s[1])*60)+(int(s[2]))


def nextAlarm():
    global sysTime
    smallest = 86400
    for turnTime in turnTimes:
        if toSeconds(turnTime) < toSeconds(sysTime):
            print(turnTime + " has already passed")
        elif toSeconds(turnTime) < smallest:
            smallest = toSeconds(turnTime)
    if smallest == 86400:
        return smallest + toSeconds(turnTimes[0])
    else:
        return smallest


def sleepRemainingTime():
    setTime()
    global sysTime
    print("Waiting for " + str(nextAlarm() - toSeconds(sysTime)) + " seconds")
    time.sleep(nextAlarm() - toSeconds(sysTime))
    print("Done!")
