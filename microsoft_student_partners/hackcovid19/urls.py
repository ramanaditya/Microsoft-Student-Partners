from django.urls import path
from django.views.generic.base import TemplateView

from microsoft_student_partners.hackcovid19.views import Hackcovid19

app_name = "hackcovid19"
urlpatterns = [
    path("", view=Hackcovid19.as_view(), name="home"),
]
