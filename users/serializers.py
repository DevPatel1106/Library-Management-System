from rest_framework import serializers

from .models import UserProfile

from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
# from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage,send_mail

import smtplib
from email.mime.text import MIMEText
from Libraryms.settings import EMAIL_HOST_USER,EMAIL_HOST_PASSWORD

from django.contrib.auth.tokens import default_token_generator

class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model=UserProfile
        fields = ['email','username','password','password2']
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def save(self):
        profile = UserProfile(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})
        profile.set_password(password)
        profile.is_active=False

        # # current_site = get_current_site(request)
        # mail_subject = 'Account created.'
        # message =  {
        #     'user': profile,
        #     # 'domain': current_site.domain,
        #     # 'uid':urlsafe_base64_encode(force_bytes(account.pk)),
        #     'uid':profile.pk,
        #     # 'token':account_activation_token.make_token(account),
        # }
        # to_email = self.validated_data['email']
        # email = EmailMessage(
        #         mail_subject, message, to=[to_email]
        # )
        # email.send()

        # body = message
        # # make up message
        # msg = body
        # msg['Subject'] = 'theme'
        # msg['From'] = EMAIL_HOST_USER
        # msg['To'] = ", ".join(to_email)
        # #sending
        # session = smtplib.SMTP('smtp.gmail.com', 587)
        # session.starttls()
        # session.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        # send_it = session.sendmail(EMAIL_HOST_USER, to_email, msg.as_string())
        # session.quit()
        activate_link_url='http://127.0.0.1:8000/users/register/verify/'
        confirmation_token = default_token_generator.make_token(profile)
        print(confirmation_token)
        mess= f'{activate_link_url}?user_id={profile.email}&confirmation_token={confirmation_token}'
        send_mail(
            subject='Email verification',
            message=("This mail is to verify your mail.TO verify click on:"+mess),
            from_email=EMAIL_HOST_USER,
            recipient_list=[profile,]
        )

        profile.save()
        return profile
    