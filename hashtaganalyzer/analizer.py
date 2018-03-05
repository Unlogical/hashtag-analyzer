from textblob import TextBlob
from hashtaganalyzer import twitter_functions

pos_threshold = 0.4
neg_threshold = -0.3


def pos_tweets(tweets):
    pos_tweets = []
    for tweet in tweets:
        tweet = TextBlob(tweet)
        if tweet.polarity > pos_threshold:
            pos_tweets.append(tweet)
    return pos_tweets


def neg_tweets(tweets):
    neg_tweets = []
    for tweet in tweets:
        tweet = TextBlob(tweet)
        if tweet.polarity < neg_threshold:
            neg_tweets.append(tweet)
    return neg_tweets

def neu_tweets(tweets):
    neu_tweets = []
    for tweet in tweets:
        tweet = TextBlob(tweet)
        if tweet.polarity <= pos_threshold and tweet.polarity >= neg_threshold:
            neu_tweets.append(tweet)
    return neu_tweets
