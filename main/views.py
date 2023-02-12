from django.shortcuts import render
# Create your views here.

from rest_framework.views import APIView
from .serializers import BookSerializer, BookReviewSerializer, IssueSerializer, LateSerializer, ReserveSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Book, BookReviews
from .models import IssueReport as IssueReportModel
from .models import LateReport as LateReportModel
from .models import ReserveReport as ReserveReportModel
import razorpay
from Libraryms.settings import RAZORPAY_API_SECRET_KEY, RAZORPAY_API_KEY


from rest_framework_swagger.views import get_swagger_view

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


class BookReviewList(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = BookReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        bookreviews = BookReviews.objects.all()
        serializer = BookReviewSerializer(bookreviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IssueReport(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, format=None):
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        reports = IssueReportModel.objects.all()
        serializer = IssueSerializer(reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    

class LateReport(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, format=None):
        serializer = LateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        reports = LateReportModel.objects.all()
        serializer = LateSerializer(reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    

class LateReportDetail(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self, pk):
        try:
            return LateReportModel.objects.get(pk=pk)
        except LateReportModel.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    def get(self, request, pk, fromat=None):
        report = self.get_object(pk)
        serializer = LateSerializer(report)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def put(self, request, pk, fromat=None):
        report = self.get_object(pk)
        serializer = LateSerializer(report, data= request.data)
        if serializer.is_valid():
            serializer.save(request)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReserveReport(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = ReserveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        reports = ReserveReportModel.objects.all()
        serializer = ReserveSerializer(reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    


client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def pay(request):

    if request.POST==True:
        razorpay_payment_id = request.razorpay_payment_id
        razorpay_order_id  = request.razorpay_order_id
        razorpay_signature = request.razorpay_signature

        bool = client.utility.verify_payment_signature({
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        })


    amount = 10000
    amount_disp = 100
    DATA = {
        "amount": amount,
        "currency": "INR",
    }
    pay_order = client.order.create(data=DATA)
    pay_order_id = pay_order['id']

    context = {
        'amount': amount,
        'api_key': RAZORPAY_API_KEY,
        'order_id': pay_order_id,
        'amount_disp' : amount_disp,
    }
    return render(request,'payment.html',context)


