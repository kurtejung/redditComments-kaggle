
## Program to determine the most controversial words in reddit comments for May 2015
## Kurt Jung, Jan 26, 2015

import sqlite3
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import urllib

useExtDict = 0

sql_conn = sqlite3.connect('../input/database.sqlite')
res_part2 = pd.read_sql("SELECT body, controversiality FROM May2015 ORDER BY controversiality DESC LIMIT 1000000", sql_conn)

### note in principle these must be scaled by the word frequency table for regular speech
wordFreqTab = {}

## unfortunately kaggle does not allow external downloads in scripts so we can't divide all hits by their natural frequency...
## but i'll keep the functionality here in case this is allowed in the future
#urllib.request.urlretrieve('http://web.ics.purdue.edu/~jung68/written.al','dict.al')
if useExtDict:
    with open('dict.al') as f:
        for fline in f:
            fwords = fline.split()
            # set the frequency of word fwords[1]
            wordFreqTab[fwords[1]] = fwords[0]

wordarr = {}

#remove most commonly used articles that don't tell us much
words_to_ignore = ['and','the','of','a','in','to','it','i','that','for','with','on','this','they','at','but','from','by','is','are','be','if','was','as','or','so']

# sum controversy score for each word in all comments
print(res_part2.keys())
for index,values in res_part2.iterrows():
    words = values['body'].split()
    for word in words:
        word = word.lower()
        if(word in words_to_ignore):
            continue
        elif( word in wordarr):
            wordarr[word] += values['controversiality']
        else:
            wordarr[word] = values['controversiality']

## functionality that would be used if i could load the word frequency table - scale the results by the natural word frequency
if useExtDict:
	for word in wordarr:
		if word in wordFreqTab:
			wordarr[word] /= wordFreqTab[word]

# print out 20 most controversial words
for i,word in enumerate(sorted(wordarr, key=wordarr.get, reverse=True)):
    if(i<20):
        print(word, " ", wordarr[word])

