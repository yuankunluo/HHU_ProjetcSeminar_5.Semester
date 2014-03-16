import csv
import matplotlib.pyplot as plt
import datetime

year = []
month = []
day = []

csv_in = open("rihanna.csv", "rb")
reader = csv.reader(csv_in)

for row in reader:
    date = datetime.datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
    print date
    year.append([date.strftime("%Y")])
    month.append([date.strftime("%m")])
    day.append([date.strftime("%d")])

x = [date for (date, value) in date]
y = [value for (date, value) in date]

fig = plt.figure()

graph = fig.add_subplot(111)
graph.plot_date(x,y)

plt.show()
# print month
