from textblob import TextBlob
from hashtaganalyzer import twitter_functions

def pos_tweets(tweets):
    pos_tweets = []
    for tweet in tweets:
        tweet = TextBlob(tweet)
        if tweet.polarity > 0.1:
            pos_tweets.append(tweet)
    return pos_tweets


def neg_tweets(tweets):
    neg_tweets = []
    for tweet in tweets:
        tweet = TextBlob(tweet)
        if tweet.polarity < -0.1:
            neg_tweets.append(tweet)
    return neg_tweets

def neu_tweets(tweets):
    neu_tweets = []
    for tweet in tweets:
        tweet = TextBlob(tweet)
        if tweet.polarity <= 0.1 and tweet.polarity >= -0.1:
            neu_tweets.append(tweet)
    return neu_tweets
