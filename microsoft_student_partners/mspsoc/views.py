import json

import pandas as pd
from django.conf import settings
from django.shortcuts import render
from django.views import View
import datetime
from microsoft_student_partners.github.views import GitHub
import os.path
import csv
from os import path

from microsoft_student_partners.twitter.views import Twitter

ROOT_DIR = settings.ROOT_DIR
THIS_DIR = str(ROOT_DIR) + "/microsoft_student_partners/mspsoc/"


class Mspsoc(View):
    template_name = "mspsoc/index.html"

    def get(self, request, *args, **kwargs):
        with open("microsoft_student_partners/mspsoc/organizers.json") as json_file:
            organizers = json.load(json_file)
        return render(request, self.template_name, context={"organizers": organizers})


class Project(View):
    template_name = "mspsoc/project.html"

    def get(self, request, *args, **kwargs):
        context = {}
        fetched_info = []
        if os.path.isfile(str(THIS_DIR) + "project.json"):
            with open(
                "microsoft_student_partners/mspsoc/projects_list.json"
            ) as json_file:
                fetched_info = json.load(json_file)
            for info in fetched_info:
                temp_dict = {}
                for key, val in info.items():
                    temp_dict[key] = val
                    context.update(temp_dict)

        gh = GitHub()

        new_fetched_info = []
        with open("microsoft_student_partners/mspsoc/project.json") as json_file:
            project_list = json.load(json_file)["projects"]

        for project in project_list:
            if project["repository"] not in context.keys():
                data = dict()

                repo_details = gh.get_repository(
                    project["username"], project["repository"]
                )
                if repo_details:
                    data[project["repository"]] = repo_details

                data[project["repository"]]["languages"] = {}
                languages = gh.get_language_repo(
                    project["username"], project["repository"]
                )
                if languages:
                    data[project["repository"]]["languages"] = languages

                new_fetched_info.append(data)

                # Writing to sample.json
                context.update(data)
            if new_fetched_info:
                complete_info = fetched_info
                complete_info.extend(new_fetched_info)
                with open(
                    "microsoft_student_partners/mspsoc/projects_list.json", "w"
                ) as projects_list_file:
                    projects_list_file.write(json.dumps(complete_info, indent=4))
        return render(request, self.template_name, {"context": context})


class Social(View):
    template_name = "mspsoc/social.html"

    def get(self, request, *args, **kwargs):
        context = dict()
        twitter_list = []
        twitter = Twitter()
        tweets_hashtags_info = []
        tweets_df = pd.DataFrame()
        CSV_FILE = str(THIS_DIR) + "tweets.csv"
        fetched_info = []
        try:
            if os.path.isfile(str(CSV_FILE)):
                try:
                    tweets_df = pd.read_csv(CSV_FILE)
                except:
                    tweets_df = pd.DataFrame()
        except FileNotFoundError:
            pass
        if not tweets_df.empty or datetime.datetime.now().hour % 2 == 0:
            hashtags = "mspsoc"
            date = "2020-05-05"
            fetched_info = twitter.search_hashtags(hashtags, date)
            with open(str(THIS_DIR) + "tweets.csv", "w") as csv_file:
                csv_writer = csv.writer(csv_file)
                for pair in fetched_info:
                    row = []
                    for key, val in pair.items():
                        row.append(val)
                    csv_writer.writerow(row)
            csv_file.close()
        if not tweets_df.empty or fetched_info:
            print("NO ERROR")
            tweets_df = pd.read_csv(CSV_FILE, delimiter=",")
            print("READ")
            if not tweets_df.empty:
                print("EMPTY")
                for index, row in tweets_df.iterrows():
                    temp = dict()
                    temp["username"] = row[0]
                    temp["name"] = row[1]
                    temp["background_color"] = row[2]
                    temp["image"] = row[3]
                    temp["tweet"] = row[4]
                    twitter_list.append(temp)

        context["twitter"] = twitter_list
        return render(request, self.template_name, {"context": context})
