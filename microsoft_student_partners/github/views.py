import json

import requests
from django.conf import settings
from django.http import JsonResponse


# Create your views here.


class GitHub:
    def __init__(self):

        self.GITHUB_OAUTH_TOKEN = settings.GITHUB_OAUTH_TOKEN
        self.GITHUB_USERNAME = settings.GITHUB_USERNAME

        self.GH_SESSION = requests.Session()
        self.GH_SESSION.auth = (self.GITHUB_USERNAME, self.GITHUB_OAUTH_TOKEN)

    def get_repository(self, user=None, repo=None):
        REPOS_URL = "https://api.github.com/repos/" + user + "/" + repo
        try:
            repository = json.loads(self.GH_SESSION.get(REPOS_URL).text)
        except:
            repository = {}
        return repository

    def get_language_repo(self, user=None, repo=None):
        LANG_URL = "https://api.github.com/repos/" + user + "/" + repo + "/languages"
        try:
            languages = json.loads(self.GH_SESSION.get(LANG_URL).text)
        except:
            languages = {}
        return languages
