
## Simple program to track decay of memes or current events
## K. Jung, Jan. 26, 2016

## For use only with the Kaggle database of Reddit Comments from May 2015
## https://www.kaggle.com/reddit/reddit-comments-may-2015

import sqlite3
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import datetime
import matplotlib.pyplot as plt

memes = ["jet fuel","nepal"]

## Filter query for meme keywords to avoid 8 GB mem limit for all score>0
query = "SELECT created_utc, body FROM May2015 WHERE score > 0 AND body LIKE '%nepal%' OR body LIKE '%jet fuel%' "

sql_conn = sqlite3.connect('../input/database.sqlite')
res = pd.read_sql(query, sql_conn)
memeCounter = []
for i in range(0,len(memes)):
    tempCounter = []
    for j in range(0,32):
        tempCounter.append(0)
    memeCounter.append(tempCounter)
timestamps = np.arange(0.0,32.0,1)

#count mentions of each keyword in SQL output
for index,values in res.iterrows():
    timest = int(values['created_utc'])
    ts = int(datetime.datetime.fromtimestamp(int(timest)).strftime('%d'))
    #ts += int(datetime.datetime.fromtimestamp(int(timest)).strftime('%-H'))
    comment = values['body']
    counter = 0
    for meme in memes:
        if meme.lower() in comment:
            memeCounter[counter][ts]+=1
        counter+=1

# ...and plot it
fig, ax = plt.subplots(1,1)
plot1 = ax.plot(timestamps,memeCounter[2], label="Jet Fuel")
plot2 = ax.plot(timestamps,memeCounter[3], 'r-', label="Nepal")
plt.legend(loc=2)
    
ax.set_ylabel('Mentions')
ax.set_xlabel('Date in May')
plt.show()
plt.savefig("MemeDecay.png")