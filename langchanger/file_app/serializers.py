from abc import ABC

from rest_framework import serializers

from .models import UserIcon, OriginIcon, AchievementIcon, OriginFile, VersionFile
from .bot import get_file, send_file, send_image


def validate_file(value):
    max_file_size = 3 * 1024 ** 2
    acceptable_format = 'txt'

    if value['file'].size > max_file_size:
        raise serializers.ValidationError('File is too big (max size - 3 Mb)')

    if value['file'].name[-3:] != acceptable_format:
        raise serializers.ValidationError(f'The unacceptable format (acceptable format \'{acceptable_format}\')')

    return value


def validate_image(value):
    max_image_size = 3 * 1024 ** 2

    if value:
        if value['image'].size > max_image_size:
            raise serializers.ValidationError("Icon is too big (max size - 3 Mb)")

    return value


class FileUrlField(serializers.Field):

    def to_representation(self, value):
        try:
            file = get_file(value.tg_hash)
        except Exception:
            file = None
        return file

    def to_internal_value(self, data):
        ret = {
            'file': data,
            'tg_hash': None
        }
        return ret


class ImageUrlField(serializers.Field):

    def to_representation(self, value):
        try:
            file = get_file(value.tg_hash)
        except Exception:
            file = None
        return file

    def to_internal_value(self, data):
        ret = {
            'image': data,
            'tg_hash': None
        }
        return ret


class FileSerializer(serializers.ModelSerializer):
    file = FileUrlField(source='*', validators=[validate_file])

    class Meta:
        fields = ('file', )


class IconSerializer(serializers.ModelSerializer):
    image = ImageUrlField(source='*', validators=[validate_image])

    class Meta:
        fields = ('image', )


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


