import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

tweetFile = open("tweet.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

polarity = []
subjectivity = []

for i in range(len(tweetData)):
    tb = TextBlob(tweetData[i]['text'])
    polarity.append(tb.polarity)
    subjectivity.append(tb.subjectivity)

print(polarity)
print(subjectivity)

#AVERAGE POLARITY
sum = 0
average = 0
for i in range(len(polarity)):
    sum += polarity[i]
average = sum / len(polarity)
print(average)

#AVERAGE SUBJECTIVITY
sum = 0
average = 0
for i in range(len(subjectivity)):
    sum += subjectivity[i]
average = sum / len(subjectivity)
print(average)

#HISTOGRAM FOR POLARITY
plt.hist(polarity, bins=10)
plt.xlabel('Polarity')
plt.ylabel('Number of Tweets')
plt.title('Polarity of Tweets')
plt.axis([-0.5, 1, 0, 55])
plt.grid(False)
plt.show()

# HISTOGRAM FOR SUBJECTIVITY
plt.hist(subjectivity, bins=10)
plt.xlabel('Subjectivity')
plt.ylabel('Number of Tweets')
plt.title('Subjectivity of Tweets')
plt.axis([0, 1, 0, 40])
plt.grid(False)
plt.show()

 #SCATTERPLOT
plt.plot(polarity, subjectivity, 'ro')
plt.xlabel('polarity')
plt.ylabel('subjectivity')
plt.title('Polarity and Subjectivity')
plt.axis([-1, 1.5, -1, 1.5])
plt.show()

all_tweets = ""
for i in range(len(tweetData)):
    all_tweets += tweetData[i]['text']

all = TextBlob(all_tweets)
filteredWords = {}
all.words
for words in 



print(all_tweets)
