from django.shortcuts import render
from . import twitter_functions

# Create your views here.
def input(request):
    return render(request, 'hashtaganalyzer/input.html', {})

def tweets(request):
    tweets = twitter_functions.get_tweets()
    return render(request, 'hashtaganalyzer/tweets.html', {'tweets': tweets})