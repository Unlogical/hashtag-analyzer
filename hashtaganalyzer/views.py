from django.shortcuts import render
from django.template import RequestContext

from hashtaganalyzer.forms import HashtagForm
from . import twitter_functions
from . import analizer

# Create your views here.
# def input(request):
#     form = HashtagForm()
#     return render(request, 'hashtaganalyzer/input.html', {'form': form})

# def tweets(request):
#     tweets = twitter_functions.get_tweets('why')
#     return render(request, 'hashtaganalyzer/tweets.html', {'tweets': tweets})


def search(request):
    if request.method == 'POST': # If the form has been submitted...
        form = HashtagForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            hashtag =  form.cleaned_data['hashtag']
            hashtag = hashtag.replace('#', '')
            tweets = twitter_functions.get_tweets(hashtag)
            tweets = twitter_functions.clear_tweets(tweets)
            pos_tweets, neg_tweets, neu_tweets = analizer.tweets_analyze(tweets)
            return render(request, 'hashtaganalyzer/tweets.html', {'pos_tweets': pos_tweets, 'neg_tweets': neg_tweets, 'neu_tweets': neu_tweets, 'hashtag': hashtag}) # Redirect after POST
    else:
        form = HashtagForm() # An unbound form

    return render(request, 'hashtaganalyzer/input.html', {'form': form }, RequestContext(request))