from django.shortcuts import render
import json
import tweepy
import requests
from django.conf import settings

# Create your views here.


class Twitter:
    def __init__(self):
        self.TWITTER_CONSUMER_API_KEY = settings.TWITTER_CONSUMER_API_KEY
        self.TWITTER_CONSUMER_SECRET_KEY = settings.TWITTER_CONSUMER_SECRET_KEY
        self.TWITTER_ACCESS_TOKEN = settings.TWITTER_ACCESS_TOKEN
        self.TWITTER_ACCESS_TOKEN_SECRET = settings.TWITTER_ACCESS_TOKEN_SECRET

        auth = tweepy.OAuthHandler(
            self.TWITTER_CONSUMER_API_KEY, self.TWITTER_CONSUMER_SECRET_KEY
        )
        auth.set_access_token(
            self.TWITTER_ACCESS_TOKEN, self.TWITTER_ACCESS_TOKEN_SECRET
        )

        self.TWITTER_API = tweepy.API(auth)

    def get_twitter_user(self, user="mspsoc"):
        user = self.TWITTER_API.get_user(user)
        return user._json

    def search_hashtags(self):
        data = []
        for tweet in tweepy.Cursor(
            self.TWITTER_API.search,
            q=("#mspsoc", "#60daysofmspsoc", "#codewithmspsoc"),
            since="2020-05-05",
        ).items():
            data.append(tweet._json)
        print(data)
        return data
