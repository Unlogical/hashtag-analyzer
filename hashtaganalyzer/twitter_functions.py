
import tweepy
from hashtagproject.settings import TWITTER_FEED_OPEN_AUTH_SECRET, TWITTER_FEED_CONSUMER_PUBLIC_KEY, \
    TWITTER_FEED_CONSUMER_SECRET, TWITTER_FEED_OPEN_AUTH_TOKEN

consumer_key = TWITTER_FEED_CONSUMER_PUBLIC_KEY
consumer_secret = TWITTER_FEED_CONSUMER_SECRET
access_token = TWITTER_FEED_OPEN_AUTH_TOKEN
access_token_secret = TWITTER_FEED_OPEN_AUTH_SECRET


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)