from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class Hackcovid19(View):
    template_name = "hackcovid19/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
