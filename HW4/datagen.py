#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import csv
data = []
with open('kernel.log', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        if 'urrsched:' in row and 'PID' in row and 'weight' in row:
            parsedrow = []
            for item in row[8:]:
                try:
                    parsedrow.append(int(item))
                except ValueError:
                    pass
            data.append(np.array(parsedrow))
#make data into numpy array
data = np.array(data)
#print('Example input string that we are parsing:')
#print('urr_task_tick PID 3482 with weight 1 timeslice 10 RUNtime 162985252280 ACTUALtime 309785010174 tick_count 16751')
#PID WEIGHT TIMESLICE RUNTIME ACTUALTIME TICK

#plot the data
starttime_ns = data[0][4]
print(data[1][4] - starttime_ns)
x = []
y = []
xlabels = ['Time']
#data = np.sort(data, axis=0)

#print(data)
for line in data:
    x.append( (line[4] - starttime_ns) * (10**-6) ) # the time is added to the x
    y.append(line[1])

#print(x[0])
#print(y[0])
x = np.array(x)
y = np.array(y)
plt.plot(x, y, 'ro')
# You can specify a rotation for the tick labels in degrees or with keywords.
#plt.xticks(x, xlabels, rotation='vertical')
plt.title('Execution of User Round Robin Processes over time')
plt.ylabel('Process Weight')
plt.xlabel('Time in ms')
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.15)
plt.show()
