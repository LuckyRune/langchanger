from rest_framework import serializers

from .models import *
from django.contrib.auth.models import User
from translation_app.serializers import MainInfoOriginSerializer


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        fields = ('id', 'name', 'description', 'rate', 'icon')


class UserProfileSerializer(serializers.ModelSerializer):

    user = BaseUserSerializer
    achievements = AchievementSerializer(many=True)
    on_hold = MainInfoOriginSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ('user', 'rate', 'description', 'achievements', 'on_hold', 'profile_icon')


class AllUserProfileSerializer(serializers.ModelSerializer):

    user = BaseUserSerializer

    class Meta:
        model = UserProfile
        fields = ('user', 'rate', 'profile_icon')



