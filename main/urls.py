from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('booklist/', views.BookList.as_view(), name='ListOfBooks'),
    path('bookdetail/<int:pk>/', views.BookDetail.as_view(), name='DetailOfBook'),
]

urlpatterns = format_suffix_patterns(urlpatterns)