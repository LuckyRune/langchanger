from rest_framework import serializers

from .models import *
from django.contrib.auth.models import User


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        fields = ('id', 'name', 'description', 'rate', 'icon')


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'rate', 'description', 'achievements', 'on_hold', 'profile_icon')


class DetailedUserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_profile')


class AllUserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'rate', 'profile_icon')


class AllUserSerializer(serializers.ModelSerializer):
    user_profile = AllUserProfileSerializer()
    count_achievement = serializers.IntegerField(read_only=True)
    count_translation = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_profile', 'count_achievement', 'count_translation')


class RateUserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'rate')


class RateUserSerializer(serializers.ModelSerializer):

    user_profile = RateUserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'user_profile')


class SettingUserSerializer(serializers.ModelSerializer):

    user_profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_profile')

