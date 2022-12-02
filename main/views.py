from django.shortcuts import render
# Create your views here.

from rest_framework.views import APIView
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Book

class BookList(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookDetail(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    def get(self, request, pk, fromat=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def put(self, request, pk, fromat=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book=self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)