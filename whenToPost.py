
## Program to determine best time to post reddit for May 2015
## Kurt Jung, Jan 26, 2015

import sqlite3
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import datetime
import string
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import urllib

useExtDict = 0

def func(x, a, b, c):
    return a * np.sin(b *2 * np.pi * x) + c

sql_conn = sqlite3.connect('../input/database.sqlite')

#read in all queries at once to avoid late errors from random db corruption
res = pd.read_sql("SELECT created_utc, score FROM May2015 WHERE score > 10 ORDER BY score DESC", sql_conn)
res_part2 = pd.read_sql("SELECT body, controversiality FROM May2015 ORDER BY controversiality DESC LIMIT 10000", sql_conn)

## First look at the average score per minute
## See that maximum value occurs ~12:30 PM UTC (8:30 AM US/NYC)
timestamps = np.arange(0.0,1440.0,1)
scores = []
nentriesPerHour = []
for i in range(0,1440):
    scores.append(0)
    nentriesPerHour.append(0)

print(res.keys())
for index,values in res.iterrows():
    timest = int(values['created_utc'])
    sc = values['score']
    ts = int(datetime.datetime.fromtimestamp(int(timest)).strftime('%-H'))*60
    ts += int(datetime.datetime.fromtimestamp(int(timest)).strftime('%-M'))
    scores[ts] += sc
    nentriesPerHour[ts]+=1
    ts += float(datetime.datetime.fromtimestamp(int(timest)).strftime('%-S'))/3600.
    #timestamps.append(ts)

for elem in range(0,1440):
    if(nentriesPerHour[elem] > 0):
        scores[elem] /= nentriesPerHour[elem]

fitcurve = func(timestamps,300,900,600)
popt, pcov = curve_fit(func, timestamps, scores)

fig, ax = plt.subplots(1, 1)
ax.plot(timestamps, scores)

#tried fitting a few functional forms (exp, sinusoid, linear) but the fit is terrible - 
#ax.plot(timestamps, func(timestamps, *popt), 'r-', label="Fit")
ax.set_ylabel('Average Score')
ax.set_xlabel('Time of day (UTC minutes)')
plt.savefig("scoreVtime.png")
