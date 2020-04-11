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


class PostUserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('description', 'profile_icon')


class SettingUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(username=self.validated_data['username'],
                    email=self.validated_data['email'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})

        user.set_password(password)
        user.save()

        return user

