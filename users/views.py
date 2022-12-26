from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny

from django.contrib.auth.tokens import default_token_generator
from .models import UserProfile

class UserRegistration(APIView):
    permission_classes=[AllowAny]
    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            token= Token.objects.get(user=account).key
            data['serializer_data']=serializer.data
            data['token']=token
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        user_id = request.query_params.get('user_id', '')
        confirmation_token = request.query_params.get('confirmation_token', '')
        print(confirmation_token+"    2")
        try:
            user = UserProfile.objects.get(email=user_id)
        except UserProfile.DoesNotExist:
            return Response('User not found', status=status.HTTP_400_BAD_REQUEST)
        
        if default_token_generator.check_token(user, confirmation_token) == False:
            return Response('Token is invalid or expired. Please request another confirmation email by signing in.', status=status.HTTP_400_BAD_REQUEST)
        
        user.is_active = True
        user.save()
        return Response('Email successfully confirmed')


class StaffRegistration(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            account.is_staff = True
            account.save()
            token= Token.objects.get(user=account).key
            data['serializer_data']=serializer.data
            data['token']=token
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)