from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('booklist/', views.BookList.as_view(), name='ListOfBooks'),
    path('bookdetail/<int:pk>/', views.BookDetail.as_view(), name='DetailOfBook'),
    path('bookreviewlist/', views.BookReviewList.as_view(), name='ListOfBookReviews'),
    path('issuereport/', views.IssueReport.as_view(), name='Issuereports'),
    path('latereport/', views.LateReport.as_view(), name='latereports'),
    path('reservereport/', views.ReserveReport.as_view(), name='reservereports'),
    path('LateReportDetail/<int:pk>/', views.LateReportDetail.as_view(), name='LateReportOfBook'),
    path('payment/',views.pay, name='pay')
]


urlpatterns = format_suffix_patterns(urlpatterns)