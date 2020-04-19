import json

from django.shortcuts import render
from django.views import View


class Qpower(View):
    template_name = "qpower/index.html"

    def get(self, request, *args, **kwargs):
        organizers = dict()
        with open("microsoft_student_partners/qpower/organizers.json") as json_file:
            organizers = json.load(json_file)
        return render(request, self.template_name, context={"organizers": organizers})
