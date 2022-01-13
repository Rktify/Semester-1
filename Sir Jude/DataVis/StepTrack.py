import csv
import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
import pygal

weekday = {}
weekend = {}
filename = 'Activity.csv'

with open(filename,"r") as f:
    reader = csv.reader(f)
    header = next(reader)

    n = 0
    for row in reader:
        steps = row[0]
        # Ignore NA step values
        if steps == "NA":
            steps = 0
            n += 1
        interval = int(row[2])
        time = pd.Timestamp(row[1])
        if time.dayofweek > 5:
            row.append("weekend")
            weekday.setdefault(interval,[])
            weekday[interval].append(int(steps))
        elif time.dayofweek < 5:
            row.append("weekday")
            weekend.setdefault(interval,[])
            weekend[interval].append(int(steps))

    dayavg= []
    for i in weekday.keys():
        dayavg.append(st.mean(weekday.get(i)))

    endavg = []
    for i in weekend.keys():
        endavg.append(st.mean(weekend.get(i)))

    hist = pygal.Bar()
    hist.title = "Weekday Average Step"
    hist.x_title = "The Interval"
    hist.y_title = "Average per interval"
    hist.x_labels = weekday.keys()
    hist.add("Average steps",dayavg)
    hist.render_to_file('weekdaysteps.svg')

    hist = pygal.Bar()
    hist.title = "Weekend Average Step"
    hist.x_title = "The Interval"
    hist.y_title = "Average per interval"
    hist.x_labels = weekend.keys()
    hist.add("Average steps",endavg)
    hist.render_to_file('weekendsteps.svg')