import base64
import os
import fitz
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.views import View
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail,
    Attachment,
    FileContent,
    FileName,
    FileType,
    Disposition,
    ContentId,
)


# import pandas as pd

# Create your views here.


class Certificate:
    def certificate(self, first_name, last_name, event_name, email_id):
        IMG_DIR, img_name = self.write_image(first_name, last_name, event_name)
        pdf_file = self.generate_pdf(IMG_DIR, img_name)
        # email = self.send_email(email_id, pdf_file)
        return img_name

    def write_image(self, first_name, last_name, event_name):
        """Getting Path"""
        ROOT_DIR = settings.ROOT_DIR
        IMG_DIR = str(ROOT_DIR) + "/microsoft_student_partners/certificates/"
        img = Image.open(IMG_DIR + "msp_certificate.png")

        """Font Family"""
        fnt_regular = ImageFont.truetype(
            IMG_DIR + "Libre_Baskerville/LibreBaskerville-Regular.ttf", size=16
        )
        fnt_bold = ImageFont.truetype(
            IMG_DIR + "Libre_Baskerville/LibreBaskerville-Bold.ttf", size=18
        )
        fnt_italic = ImageFont.truetype(
            IMG_DIR + "Libre_Baskerville/LibreBaskerville-Italic.ttf", size=45
        )
        fnt_url = ImageFont.truetype(
            IMG_DIR + "Libre_Baskerville/LibreBaskerville-Italic.ttf", size=10
        )

        """Writing to Image"""
        d = ImageDraw.Draw(img)

        """Writing the name and event name"""
        d.text(
            (70, 285), first_name, font=fnt_italic, fill=(0, 120, 212),
        )
        d.text(
            (65, 345), last_name, font=fnt_italic, fill=(0, 120, 212),
        )
        d.text(
            (70, 520), event_name, font=fnt_bold, fill=(0, 0, 0),
        )

        """Writing remaining Texts"""
        d.text(
            (68, 220),
            "This certificate is presented to :",
            font=fnt_regular,
            fill=(0, 0, 0),
        )
        d.text(
            (68, 450),
            "In recognition of your attendance and completion of the",
            font=fnt_regular,
            fill=(0, 0, 0),
        )
        d.text(
            (68, 480), "Microsoft Student Partners", font=fnt_regular, fill=(0, 0, 0),
        )

        """Writing details of Issuer"""
        d.text(
            (70, 650), "Aditya Raman", font=fnt_bold, fill=(0, 0, 0),
        )
        d.text(
            (70, 675),
            "Beta Student Partner | Microsoft Student Partners",
            font=fnt_regular,
            fill=(0, 0, 0),
        )

        """Writing Verification Link"""
        unique_id = get_random_string(length=10).upper()
        d.text(
            (510, 800), "Verify at : ", font=fnt_regular, fill=(0, 0, 0),
        )
        d.text(
            (600, 800),
            "https://mspglobal.azurewebsites.net/certificates/" + unique_id,
            font=fnt_regular,
            fill=(0, 0, 0),
        )

        """Saving Image"""
        IMG_SAVE_DIR = str(ROOT_DIR) + "/microsoft_student_partners/media/"
        os.mkdir(IMG_SAVE_DIR)
        img_name = first_name + "_" + last_name
        img.save(IMG_SAVE_DIR + img_name + ".png")
        img_path = IMG_SAVE_DIR + img_name + ".png"
        print("IMG_PATH : ", img_path)
        return IMG_SAVE_DIR, img_name

    def generate_pdf(self, IMG_DIR, img_name):
        img_path = IMG_DIR + img_name + ".png"
        imglist = [img_path]
        doc = fitz.open()  # PDF with the pictures
        for i, f in enumerate(imglist):
            img = fitz.open(f)  # open pic as document
            rect = img[0].rect  # pic dimension
            pdfbytes = img.convertToPDF()  # make a PDF stream
            img.close()  # no longer needed
            imgPDF = fitz.open("pdf", pdfbytes)  # open stream as PDF
            page = doc.newPage(
                width=rect.width, height=rect.height  # new page with ...
            )  # pic dimension
            page.showPDFpage(rect, imgPDF, 0)
            # image fills the page

        """Saving the pdf"""
        doc.save(IMG_DIR + img_name + ".pdf")
        pdf_file = IMG_DIR + img_name + ".pdf"
        return pdf_file

    def send_email(self, email, pdf_path):
        message = Mail(
            from_email="Aditya Raman <adityaraman96@gmail.com>",
            to_emails=email,
            subject="[MSP Testing] Testing for Attendee's Certificate",
            html_content=" Sending the attachment<br>",
        )

        file_path = pdf_path
        file_name = list(file_path.split("/"))[-1]
        with open(file_path, "rb") as f:
            data = f.read()
            f.close()
        encoded = base64.b64encode(data).decode()
        attachment = Attachment()
        attachment.file_content = FileContent(encoded)
        attachment.file_type = FileType("application/pdf")  # FileType("image/png")
        attachment.file_name = FileName(file_name)
        attachment.disposition = Disposition("attachment")
        attachment.content_id = ContentId("Microsoft Student Partner")
        message.attachment = attachment
        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
            return response
        except Exception as e:
            print(e)
            return e


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
