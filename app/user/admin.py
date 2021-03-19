from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NepUser

# Register your models here.

admin.site.register(NepUser, UserAdmin)