from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

class registration(APIView):
    
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