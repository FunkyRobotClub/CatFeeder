import csv
from . import timer


def log_data(sensor_reading):
    with open('/home/programming/Documents/Cat Feeder/Site/catserver/interface/Feeder/src/log.csv', 'a', newline='') \
            as logfile:
        logwriter = csv.writer(logfile)
        logwriter.writerow([timer.get_date(), sensor_reading])


def clear_data():
    with open('/home/programming/Documents/Cat Feeder/Site/catserver/interface/Feeder/src/log.csv', 'w') as logfile:
        clear = csv.writer(logfile)
        clear.writerow([])


def get_data():
    with open('/home/programming/Documents/Cat Feeder/Site/catserver/interface/Feeder/src/log.csv', 'r') as logfile:
        output = []
        logreader = csv.reader(logfile)
        for row in logreader:
            output += row
        return output
