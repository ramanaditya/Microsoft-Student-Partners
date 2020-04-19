from django.urls import path
from django.views.generic.base import TemplateView

from microsoft_student_partners.certificates.views import CertificateView

app_name = "certificates"
urlpatterns = [
    path("", view=CertificateView.as_view(), name="home"),
]
