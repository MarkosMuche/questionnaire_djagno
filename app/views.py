
from rest_framework.views import APIView
from rest_framework.response import Response
from ai_utils.utils import get_vision_statement
from django.core.mail import send_mail
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
from decouple import Config
import json



class MainView(APIView):

    def post(self, request):
        data = request.data
        print(data)
        email=data['email']
        print(email)
        config = Config('.env')
        print('solomon')
        vision_statement = get_vision_statement(data)
        email_sender=config("email_sender")
        email_password=config("email_password")
        email_receiver=email

        subject='your vision'
        body = json.dumps(vision_statement)

        em=EmailMessage()
        em['From']=email_sender
        em['To']=email_receiver
        em['subject']=subject
        em.set_content(body)

        context=ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())
        return Response('')       