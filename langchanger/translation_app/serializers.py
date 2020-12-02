from rest_framework import serializers

from file_app.serializers import OriginFileSerializer, OriginIconSerializer
from registration_app.serializers import RateUserSerializer
from .models import *


def get_user_with_rate(obj):
    users = User.objects.filter(pk=obj.author.id)

    if not users:
        return 'Deleted user'

    user = users.first()

    serializer = RateUserSerializer(user)
    return serializer.data


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name')


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('id', 'name')


class OneOriginSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    origin_language = LanguageSerializer()
    poster = OriginIconSerializer()

    class Meta:
        model = Origin
        fields = (
            'id', 'title', 'author', 'description', 'creation_date', 'genre',
            'origin_language', 'age_limit', 'poster')


class AllOriginSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    origin_language = LanguageSerializer()
    poster = OriginIconSerializer()

    class Meta:
        model = Origin
        fields = ('id', 'title', 'author', 'genre', 'origin_language',
                  'age_limit', 'poster')


class ReadOriginSerializer(serializers.ModelSerializer):
    source_link = OriginFileSerializer()

    class Meta:
        model = Origin
        fields = ('id', 'source_link')


class OriginCommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField('get_author_data')

    class Meta:
        model = CommentOrigin
        fields = ('id', 'post', 'post_date', 'origin', 'author', 'parent_comment')

    def get_author_data(self, obj):
        return get_user_with_rate(obj)


class MakeCommentOriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentOrigin
        fields = ('post', 'author', 'origin', 'parent_comment')
