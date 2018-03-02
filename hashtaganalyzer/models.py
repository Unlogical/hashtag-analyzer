from django.db import models
class Tweet:
    text = 'tweettext'
    tone = 1

    def __str__(self):
        return self.text

