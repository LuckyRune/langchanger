from rest_framework import serializers

from .models import *


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
    format_type = FormatTypeSerializer
    origin_language = LanguageSerializer

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

    class Meta:
        model = Translation
        fields = ('id', 'author')


class UserProfileTranslationSerializer(serializers.ModelSerializer):

    origin = MainInfoOriginSerializer
    language = LanguageSerializer

    class Meta:
        model = Translation
        fields = ('id', 'author', 'rate', 'origin', 'language')


class ReadTranslationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Translation
        fields = ('id', 'rate', 'author')


class ReadVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = ('id', 'change_number', 'creation_date', 'version_link')


class AllVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = ('id', 'change_number', 'creation_date')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'post', 'post_date', 'author', 'parent_comment')


class OriginCommentSerializer(serializers.ModelSerializer):

    comment = CommentSerializer

    class Meta:
        model = CommentOrigin
        fields = ('id', 'comment')





