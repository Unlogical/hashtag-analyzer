from django import forms

class HashtagForm(forms.Form):
    hashtag = forms.CharField()