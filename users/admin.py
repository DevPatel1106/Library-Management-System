from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model

# from django.contrib.auth.admin import UserAdmin
# from .models import UserProfile

# class CustomUserAdmin(UserAdmin):
#     model = UserProfile
#     list_display = ('email','is_staff','is_active','username')
#     list_filter = ('email','is_staff','is_active','username')
#     search_fields = ('email','username')
#     ordering = ('email','username')

UserProfile = get_user_model()
admin.site.register(UserProfile)