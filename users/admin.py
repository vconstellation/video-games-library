from django.contrib import admin
from .models import ProfileGamesCollection, Profile, Platform

# Register your models here.
admin.site.register(ProfileGamesCollection)
admin.site.register(Profile)
admin.site.register(Platform)
