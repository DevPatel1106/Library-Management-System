from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from .serializers import RegistrationSerializer,CodeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny

from django.contrib.auth.tokens import default_token_generator
from .models import UserProfile,CodeEmail
from rest_framework.authtoken.models import Token

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


class CodeView(APIView): 
    permission_classes=[AllowAny]
    def post(self, request, format=None):
        serializer = CodeSerializer(data=request.data)
        if serializer.is_valid():
            if CodeEmail.objects.filter(code = serializer.validated_data['code'] , email= serializer.validated_data['email']).exists()  :
                user=UserProfile.objects.get(email=serializer.validated_data['email'])
                user.is_active = True
                user.save()
                return Response('Email successfully confirmed')
            else:
                return Response({'message':'not equal'})
        else:
            print(serializer.errors)
            return Response({'message': 'Serializer is not valid'})

from django.contrib.auth import logout

class User_logout(APIView): 
    permission_classes=[IsAuthenticated]
    def get(self,request):
        logout(request)
        return Response('User Logged out successfully')