from rest_framework import serializers

from django.db.models import Sum

from .models import *
from registration_app.serializers import RateUserSerializer


def get_user_with_rate(obj):
    users = User.objects.filter(pk=obj.author.id).annotate(rate=Sum('translation_set__rate_set__rate'))

    if not users:
        return 'Deleted user'

    user = users.first()

    serializer = RateUserSerializer(user)
    return serializer.data


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
        fields = ('id', 'title', 'author', 'description', 'creation_date', 'genre',
                  'origin_language', 'format_type', 'age_limit', 'poster')


class AllOriginSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    format_type = FormatTypeSerializer()
    origin_language = LanguageSerializer()

    class Meta:
        model = Origin
        fields = ('id', 'title', 'author', 'genre', 'origin_language',
                  'format_type', 'age_limit', 'poster')


class ReadOriginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Origin
        fields = ('id', 'source_link')


class TranslationByLanguageSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField('get_author_data')

    class Meta:
        model = Translation
        fields = ('id', 'author')

    def get_author_data(self, obj):
        return get_user_with_rate(obj)


class AllTranslationSerializer(serializers.ModelSerializer):
    rate = serializers.IntegerField(read_only=True)
    author = serializers.SerializerMethodField('get_author_data')

    origin = AllOriginSerializer()
    language = LanguageSerializer()

    class Meta:
        model = Translation
        fields = ('id', 'creation_date', 'author', 'rate', 'origin', 'language')

    def get_author_data(self, obj):
        return get_user_with_rate(obj)


class MakeTranslationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Translation
        fields = ('origin', 'language', 'author')


class MakeVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = ('version_link', )

    def validate_version_link(self, value):
        max_file_size = 10 * 1023 ** 2
        acceptable_format = 'pdf'

        if value.size > max_file_size:
            raise serializers.ValidationError('File is too big')

        if value.name[-3:] != acceptable_format:
            raise serializers.ValidationError(value.name[-3:])

        return value


class ReadVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = ('id', 'creation_date', 'version_link')


class AllVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = ('id', 'creation_date')


class OriginCommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField('get_author_data')

    class Meta:
        model = CommentOrigin
        fields = ('id', 'post', 'post_date', 'origin', 'author', 'parent_comment')

    def get_author_data(self, obj):
        return get_user_with_rate(obj)


class MakeOriginCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentOrigin
        fields = ('post', 'author', 'origin', 'parent_comment')


class MakeRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = RateList
        fields = ('rate', 'user', 'translation')

    def validate_rate(self, value):
        if value not in (-1, 1):
            raise serializers.ValidationError("Rate is out of possible values")

        return value
