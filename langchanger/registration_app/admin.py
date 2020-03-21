from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    fields = ('description', 'user', 'profile_icon')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'rate')
