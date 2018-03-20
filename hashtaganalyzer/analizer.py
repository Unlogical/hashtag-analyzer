from textblob import TextBlob
from hashtaganalyzer import twitter_functions

pos_threshold = 0.4
neg_threshold = -0.3


def tweets_analyze(tweets):
    pos_tweets = []
    neg_tweets = []
    neu_tweets = []
    for tweet in tweets:
        tweet = TextBlob(tweet)
        if tweet.polarity > pos_threshold:
            pos_tweets.append(tweet)
        elif tweet.polarity < neg_threshold:
            neg_tweets.append(tweet)
        else:
            neu_tweets.append(tweet)
    return pos_tweets, neg_tweets, neu_tweets

