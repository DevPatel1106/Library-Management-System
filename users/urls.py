from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', views.registration.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
]

urlpatterns = format_suffix_patterns(urlpatterns)