from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'description', 'profile_icon', 'on_hold')
    list_display = ('user',)


@admin.register(Blacklist)
class BlacklistAdmin(admin.ModelAdmin):
    fields = ('user', 'ip')
    list_display = ('user', 'ip')

