import json

from django.shortcuts import render
from django.views import View

from microsoft_student_partners.github.views import GitHub


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
        gh = GitHub()

        with open("microsoft_student_partners/mspsoc/project.json") as json_file:
            project_list = json.load(json_file)["projects"]
        context = dict()

        for project in project_list:
            data = dict()

            repo_details = gh.get_repository(project["username"], project["repository"])
            if repo_details:
                data[project["repository"]] = repo_details

            data[project["repository"]]["languages"] = {}
            languages = gh.get_language_repo(project["username"], project["repository"])
            if languages:
                data[project["repository"]]["languages"] = languages

            context.update(data)
        print(context)
        return render(request, self.template_name, {"context": context})
