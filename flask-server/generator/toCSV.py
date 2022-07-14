import csv
import datetime
from tkinter import W
import generator.timetables as timetables
week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
times = ['8:30-10:00', '10:30-12:00', '12:30-14:00', '14:30-16:00']


def createCSV(tt, filename):
    print("Creating CSV file...")
    # d = datetime.datetime.now()
    # fileName = '{}.csv'.format(str(d).replace(":", "-"))
    try:
        path = "./generator/timetables/{}".format(filename)
        with open(path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=tt[0].keys())
            writer.writeheader()
            for e in tt:
                e["days"] = week_days[e["days"][0]] + \
                    " " + week_days[e["days"][1]]
                e["timeslots"] = times[e["timeslots"][0]] + \
                    " " + times[e["timeslots"][1]]
                writer.writerow(e)
        print("CSV file created.")
    except Exception as e:
        print("Error: {}".format(e))
