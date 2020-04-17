import json

from django.shortcuts import render
from django.views import View


class Hackcovid19(View):
    template_name = "hackcovid19/index.html"

    def get(self, request, *args, **kwargs):
        organizers = dict()
        with open(
            "microsoft_student_partners/hackcovid19/organizers.json"
        ) as json_file:
            organizers = json.load(json_file)
        return render(request, self.template_name, context={"organizers": organizers})
