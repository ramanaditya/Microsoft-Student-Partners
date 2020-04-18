from django.urls import path
from django.views.generic.base import TemplateView

from microsoft_student_partners.hackcovid19.views import Hackcovid19, Project

app_name = "hackcovid19"
urlpatterns = [
    path("", view=Hackcovid19.as_view(), name="home"),
    path("project/", view=Project.as_view(), name="project"),
    path(
        "contact/",
        TemplateView.as_view(template_name="hackcovid19/contact.html"),
        name="contact",
    ),
    path(
        "schedule/",
        TemplateView.as_view(template_name="hackcovid19/schedule.html"),
        name="schedule",
    ),
    path(
        "speakers/",
        TemplateView.as_view(template_name="hackcovid19/speakers.html"),
        name="speakers",
    ),
    path(
        "elements/",
        TemplateView.as_view(template_name="hackcovid19/elements.html"),
        name="elements",
    ),
]
