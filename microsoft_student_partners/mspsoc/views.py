import json

from django.shortcuts import render
from django.views import View

from microsoft_student_partners.github.views import GitHub
import os.path
from os import path

from microsoft_student_partners.twitter.views import Twitter


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
        if path.exists("project.json"):
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
                print("Fatching")
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
                print("Writing to file json")
                with open(
                    "microsoft_student_partners/mspsoc/projects_list.json", "w"
                ) as projects_list_file:
                    projects_list_file.write(json.dumps(complete_info, indent=4))
        return render(request, self.template_name, {"context": context})


class Social:
    template_name = "mspsoc/social.html"

    def get(self, request, *args, **kwargs):
        twitter = Twitter()
        twitter.search_hashtags()
        context = dict()

        return render(request, self.template_name, {"context": context})
