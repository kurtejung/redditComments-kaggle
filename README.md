# May2015 Reddit Comment DB (Kaggle)

These scripts are meant to analyze the Kaggle-hosted subset of all Reddit comments from May 2015 (https://www.kaggle.com/reddit/reddit-comments-may-2015).  

There are three simple python scripts used to analyze the data:

(1) whenToPost.py
 - This script analyzes all comments and calculates an average score for each minute of the day, determining the optimal time to post a comment to reddit to achieve the highest score.  The analysis output is in scoreVtime.png, where the time is in minutes since midnight (0:00 UTC)
 - We observe that the optimal time to post is roughly 2:30 PM UTC (ignoring an outlier at 2:10 AM), which corresponds to 10:30 AM US/NYC time, accounting for daylight savings time.  This suggests that many people check reddit as they wake up and tend to be more generous with upvoting posts early in the morning.  Conversely, the worst time to post is 8:20 AM UTC (4:20 AM US/NYC) when (apparently) people are more cynical as they get tired before heading to bed.
 - An alternative explanation may be that Reddit's sorting mechanism applies a weight to posts based on how long ago they were posted, sinking posts that are old and not popular.  In this situation, good posts that are posted right as people wake up in the US may simply be seen by more people and have a chance to avoid getting "sunk" due to age.  Similarly, comments that are posted right as people go to bed may not be seen by very many people and will easily get lost and not upvoted.

![scoreVTime](https://github.com/kurtejung/redditComments-kaggle/blob/master/scoreVtime.png)
 
(2) controversy.py
 - This script analyzes each word in the comments and weights each word by the total controversy score of all comments where the word is used.  In this way, more controversial words float to the top of the word list.  These results should be scaled by a dictionary of natural word frequency, but the Kaggle interface does not allow importation of external databases so it is not implemented here (though the functionality is left in the code)
 - The top 20 controversial words are (in order):

| Word | score |
|------|------|
| you  | 461435 |
| not  | 256658 |
| have |  218902 |
| just |  172227 |
| like |  154596 |
| it's |  153107 |
| people |  149125 |
| he |  144180 |
| don't |  134013 |
| your |  131379 |
| what  | 125091 |
| about |  124164 |
| all |  114374 |
| my  | 111659 |
| would |  107553 |
| an |  107007 |
| do |  106842 |
| because |  106159 |
| can |  103292 |
| we |  99303 |

Since I cannot import a word frequency list to scale by the amount of natural word usage, the conclusions are much less robust, but a few words stand out to me as indicative of controversy: "not", "just", "people", "don't", which tend to be associated with sarcastic or snippy language.  

(3) memeDecay.py
 - This code attempts to track the day-by-day usage of memes or hot words to determine how quickly they fall out of favor with the reddit general populace.  I applied a selection of score > 0, such that once a meme or current event topic is socially exhausted, the comments no longer get counted in the results.
 - The first results track two keywords: "Nepal" and "Jet Fuel".  Nepal was used as a current event benchmark, due to the two earthquakes that occurred in Nepal on April 25 (first peak) and May 12 (second peak).  The overall number of mentions in comments remains lower than the standard meme benchmark which is "Jet Fuel".  This refers to a popular sarcastic conspiracy theory regarding the Sept. 11 attacks suggesting that jet fuel does not burn hot enough to melt steel beams.  It's uncertain why this meme became popular in May, 2015, but google analytics (https://www.google.com/trends/explore#q=Jet%20fuel%20steel%20beams) suggest that the meme reached its height in this month.

 - The results of the two trends can be seen in MemeDecay.png
![memeDecay](https://github.com/kurtejung/redditComments-kaggle/blob/master/MemeDecay.png)
