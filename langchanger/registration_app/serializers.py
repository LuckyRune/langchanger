from django.contrib.auth.models import Group
from rest_framework import serializers

from file_app.serializers import UserIconSerializer
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    profile_icon = UserIconSerializer()

    class Meta:
        model = UserProfile
        fields = ('description', 'on_hold', 'profile_icon')


class DetailedUserSerializer(serializers.ModelSerializer):
    rate = serializers.IntegerField(read_only=True)

    user_profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_profile')


class IconUserProfileSerializer(serializers.ModelSerializer):
    profile_icon = UserIconSerializer()

    class Meta:
        model = UserProfile
        fields = ('profile_icon', )


class AllUserSerializer(serializers.ModelSerializer):

    user_profile = IconUserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_profile')


class RateUserSerializer(serializers.ModelSerializer):
    user_profile = IconUserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'user_profile')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('name', )


class MainUserInfoSerializer(serializers.ModelSerializer):
    user_profile = IconUserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'user_profile', 'is_staff')


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


class BlacklistSerializer(serializers.ModelSerializer):
    user = RateUserSerializer()

    class Meta:
        model = Blacklist
        fields = ('user', )


class PostBlacklistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blacklist
        fields = ('user', )
