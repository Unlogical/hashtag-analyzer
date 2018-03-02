from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.input, name='input'),
    url(r'^tweets/$', views.tweets, name='tweets'),
]