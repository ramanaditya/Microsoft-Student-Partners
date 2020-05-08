from django.shortcuts import render
import json
import tweepy
import requests
from django.conf import settings
import pandas as pd

import csv

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

    def get_twitter_user(self, user=None):
        user = self.TWITTER_API.get_user(user)
        return user._json

    def search_hashtags(self, hashtags=None, date=None):
        data = []
        for tweet in tweepy.Cursor(
            self.TWITTER_API.search, q=hashtags, since=date,
        ).items():
            row = {
                "username": tweet.user.screen_name,
                "name": tweet.user.name,
                "background_color": tweet.user.profile_background_color,
                "image": tweet.user.profile_image_url_https,
                "tweet": tweet.text.encode("utf-8"),
            }
            data.append(row)

        return data
