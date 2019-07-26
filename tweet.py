import json

tweetFile = open("tweet.json", "r")

tweetData = json.load(tweetFile)

tweetFile.close()

print("Tweet id:", tweetData[0]['text'])

for i in range(len(tweetData)):
    print("Tweet text:" + tweetData[i]["text"])

for tweet in tweetData:
    print("Tweet text:" + tweetData[tweet]["text"])
