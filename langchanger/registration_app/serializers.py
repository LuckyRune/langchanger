from rest_framework import serializers

from .models import *
from django.contrib.auth.models import User
from file_app.serializers import AchievementIconSerializer, UserIconSerializer


class AchievementSerializer(serializers.ModelSerializer):
    icon = AchievementIconSerializer()

    class Meta:
        model = Achievement
        fields = ('id', 'name', 'description', 'rate', 'icon')


class UserProfileSerializer(serializers.ModelSerializer):
    profile_icon = UserIconSerializer()

    class Meta:
        model = UserProfile
        fields = ('description', 'achievements', 'on_hold', 'profile_icon')


class DetailedUserSerializer(serializers.ModelSerializer):
    rate = serializers.IntegerField(read_only=True)

    user_profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'rate', 'user_profile')


class IconUserProfileSerializer(serializers.ModelSerializer):
    profile_icon = UserIconSerializer()

    class Meta:
        model = UserProfile
        fields = ('profile_icon', )


class AllUserSerializer(serializers.ModelSerializer):
    count_achievement = serializers.IntegerField(read_only=True)
    count_translation = serializers.IntegerField(read_only=True)
    rate = serializers.IntegerField(read_only=True)

    user_profile = IconUserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'rate', 'count_achievement', 'count_translation', 'user_profile')


class RateUserSerializer(serializers.ModelSerializer):
    rate = serializers.IntegerField(read_only=True)
    user_profile = IconUserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'rate', 'user_profile')


class PostUserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('description', )


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

