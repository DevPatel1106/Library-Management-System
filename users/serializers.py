from rest_framework import serializers

from .models import UserProfile,CodeEmail

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
from rest_framework.authtoken.models import Token

import random

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

        profile.save()
        
        cd=random.randint(10000, 99999)
        profile_code = CodeEmail(
            email=self.validated_data['email'],
            code=cd,
        )
        profile_code.save()

        mess=f'{cd}'
        send_mail(
            subject='Email verification',
            message=("This mail is to verify your mail.TO verify code is:"+mess),
            from_email=EMAIL_HOST_USER,
            recipient_list=[profile,]
        )

        return profile
    

class CodeSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    email  = serializers.EmailField()

