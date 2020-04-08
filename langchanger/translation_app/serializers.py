from rest_framework import serializers

from .models import *
from registration_app.serializers import RateUserSerializer, AllUserSerializer


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name')


class FormatTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FormatType
        fields = ('id', 'name')


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('id', 'name')


class OneOriginSerializer(serializers.ModelSerializer):

    genre = GenreSerializer(many=True)
    format_type = FormatTypeSerializer()
    origin_language = LanguageSerializer()

    class Meta:
        model = Origin
        fields = ('id', 'isbn', 'title', 'author', 'description', 'creation_date', 'genre',
                  'origin_language', 'format_type', 'age_limit', 'poster')


class MainInfoOriginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Origin
        fields = ('id', 'title', 'author', 'poster')


class AllOriginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Origin
        fields = ('id', 'title', 'author', 'genre', 'origin_language',
                  'format_type', 'age_limit', 'poster')


class ReadOriginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Origin
        fields = ('id', 'source_link')


class OriginTranslationSerializer(serializers.ModelSerializer):
    author = RateUserSerializer()

    class Meta:
        model = Translation
        fields = ('id', 'author')


class UserProfileTranslationSerializer(serializers.ModelSerializer):

    origin = MainInfoOriginSerializer()
    language = LanguageSerializer()

    class Meta:
        model = Translation
        fields = ('id', 'author', 'rate', 'origin', 'language')


class ReadTranslationSerializer(serializers.ModelSerializer):
    author = RateUserSerializer()

    class Meta:
        model = Translation
        fields = ('id', 'rate', 'author')


class MakeTranslationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Translation
        fields = ('origin', 'language', 'author')


class MakeVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = ('version_link', )


class ReadVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = ('id', 'creation_date', 'version_link')


class AllVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = ('id', 'creation_date')


class OriginCommentSerializer(serializers.ModelSerializer):
    author = AllUserSerializer()

    class Meta:
        model = CommentOrigin
        fields = ('id', 'post', 'post_date', 'author', 'parent_comment')
