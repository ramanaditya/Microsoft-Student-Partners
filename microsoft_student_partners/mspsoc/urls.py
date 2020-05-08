from django.urls import path
from django.views.generic.base import TemplateView

from microsoft_student_partners.mspsoc.views import Mspsoc, Project

app_name = "mspsoc"
urlpatterns = [
    path("", view=Mspsoc.as_view(), name="home"),
    path("project/", view=Project.as_view(), name="project"),
    path(
        "contact/",
        TemplateView.as_view(template_name="mspsoc/contact.html"),
        name="contact",
    ),
    path(
        "schedule/",
        TemplateView.as_view(template_name="mspsoc/schedule.html"),
        name="schedule",
    ),
    path(
        "speakers/",
        TemplateView.as_view(template_name="mspsoc/speakers.html"),
        name="speakers",
    ),
    path(
        "elements/",
        TemplateView.as_view(template_name="mspsoc/elements.html"),
        name="elements",
    ),
    path(
        "social",
        TemplateView.as_view(template_name="mspsoc/social.html"),
        name="social",
    ),
]
