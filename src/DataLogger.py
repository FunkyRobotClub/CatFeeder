import timer
import csv


def log_data(sensor_reading):
    with open('log.csv', 'a', newline='') as logfile:
        logwriter = csv.writer(logfile)
        logwriter.writerow([timer.get_date(), sensor_reading])


def clear_data():
    with open('log.csv', 'w') as logfile:
        clear = csv.writer(logfile)
        clear.writerow([])
