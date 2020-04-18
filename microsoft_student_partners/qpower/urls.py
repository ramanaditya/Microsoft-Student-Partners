from django.urls import path
from django.views.generic.base import TemplateView

from microsoft_student_partners.qpower.views import Qpower

app_name = "qpower"
urlpatterns = [
    path("", view=Qpower.as_view(), name="home"),
]
