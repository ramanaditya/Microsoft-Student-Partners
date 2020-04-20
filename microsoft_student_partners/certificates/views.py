from django.shortcuts import render
from django.views import View

from microsoft_student_partners.certificates.helpers import Certificate


class CertificateView(View):
    template_name = "certificates/project.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        context = {}
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        event_name = "Sample Event for Testing"  # request.POST.get("event_name")
        print(first_name, last_name, event_name, email)
        img_name = Certificate().certificate(first_name, last_name, event_name, email)
        context["pdf_file"] = img_name + ".pdf"
        context["img_file"] = img_name + ".png"
        return render(request, self.template_name, {"context": context})
