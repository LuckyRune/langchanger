from abc import ABC

from rest_framework import serializers

from .models import UserIcon, OriginIcon, AchievementIcon, OriginFile, VersionFile


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('file', )

    def validate_file(self, value):
        pass


class IconSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('image', )

    def validate_image(self, value):
        pass


class UserIconSerializer(IconSerializer):
    class Meta(IconSerializer.Meta):
        model = UserIcon


class OriginIconSerializer(IconSerializer):
    class Meta(IconSerializer.Meta):
        model = OriginIcon


class AchievementIconSerializer(IconSerializer):
    class Meta(IconSerializer.Meta):
        model = AchievementIcon


class OriginFileSerializer(FileSerializer):
    class Meta(FileSerializer.Meta):
        model = OriginFile


class VersionFileSerializer(FileSerializer):
    class Meta(FileSerializer.Meta):
        model = VersionFile


