from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'description', 'profile_icon', 'achievements', 'on_hold')
    list_display = ('user', )


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'rate', 'icon')
    list_display = ('name', 'rate')


@admin.register(Blacklist)
class BlacklistAdmin(admin.ModelAdmin):
    fields = ('user', 'ip')
    list_display = ('user', 'ip')

