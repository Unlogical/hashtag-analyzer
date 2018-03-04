from django import forms

class HashtagForm(forms.Form):
    hashtag = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))

