from datetime import datetime as dt
import time

sysTime = ""
turnTimes = ["09:00:00", "17:00:00"]


def setTime():
    global sysTime
    sysTime = str(dt.time(dt.now()))[:8].split(":")


def toSeconds(hms):
    # Turns HH:MM:SS into seconds
    print(hms)
    s = hms.split(':')
    print(s)
    return (int(s[0])*3600)+(int(s[1])*60)+(int(s[2]))


def nextAlarm():
    global sysTime
    smallest = 86400
    for turnTime in turnTimes:
        if toSeconds(turnTime) < toSeconds(sysTime):
            pass
        elif toSeconds(turnTime) < smallest:
            smallest = toSeconds(turnTime)
    return smallest


def sleepRemainingTime():
    setTime()
    global sysTime
    time.sleep(nextAlarm() - toSeconds(sysTime))
    print("Waiting for " + nextAlarm()-toSeconds(sysTime) + " seconds")
    print("It is " + sysTime)
    print("      " + toSeconds(sysTime))
