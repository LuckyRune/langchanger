from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Q, Sum
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer

from .models import *
from .serializers import *
from django.contrib.auth.models import User


def paginator(request, queryset):
    page_size = int(request.GET.get('page_size', 3))
    current_page = int(request.GET.get('current_page', 1))

    first_item = (current_page - 1) * page_size
    last_item = current_page * page_size

    queryset_part = queryset[first_item:last_item]

    return queryset_part


class MainPageView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        last_origins = Origin.objects.all()[:6]
        serializer = MainInfoOriginSerializer(last_origins, many=True)

        content = {'data': serializer.data}

        return Response(content)


class AllOriginView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    filter_name_set = {
        'format': 'format_type__in',
        'genre': 'genre__in',
        'age': 'age_limit__in',
        'language': 'origin_language__in',
    }

    def get(self, request):
        raw_filter = request.GET.get('filters', {})
        order_by = request.GET.get('order', 'relevance')

        complete_filter = {}
        for key, data in raw_filter.items():
            filter_key = self.filter_name_set[key]
            complete_filter[filter_key] = data

        queryset = Origin.objects.filter(**complete_filter)

        if order_by == 'relevance':
            queryset = queryset.annotate(rate=Sum('translation_set__rate_set__rate'))
            queryset = queryset.order_by('-rate', 'id')

        response_queryset = paginator(request, queryset)

        serializer = AllOriginSerializer(response_queryset, many=True)

        content = {'data': serializer.data}

        return Response(content)


class OneOriginView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = int(request.GET.get('origin', -1))

        origin = get_object_or_404(Origin, pk=pk)
        translation_lang = Translation.objects.filter(origin=pk).only('language').distinct()
        languages = Language.objects.filter(pk__in=translation_lang)

        serializer_language = LanguageSerializer(languages, many=True)
        serializer_origin = OneOriginSerializer(origin)

        content = {'data': {
            'origin': serializer_origin.data,
            'languages': serializer_language.data,
        }}

        return Response(content)


class TranslationByLanguageView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        origin = int(request.GET.get('origin', -1))
        language = int(request.GET.get('language', -1))

        if origin != -1 and language != -1:
            translations = Translation.objects.filter(
                Q(origin=origin) &
                Q(language=language)
            )
        else:
            raise Http404

        serializer = OriginTranslationSerializer(translations, many=True)

        content = {'data': serializer.data}

        return Response(content)


class ReadOriginView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = int(request.GET.get('origin', -1))

        origin = get_object_or_404(Origin, pk=pk)
        serializer = ReadOriginSerializer(origin)

        content = {'data': serializer.data}

        return Response(content)


class ReadTranslationView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = int(request.GET.get('translation', -1))

        translation = get_object_or_404(Translation, pk=pk)
        last_version = Version.objects.filter(translation=pk).latest('creation_date')

        serializer_translation = ReadTranslationSerializer(translation)
        serializer_version = ReadVersionSerializer(last_version)

        content = {'data': {
            'translation': serializer_translation.data,
            'last_version': serializer_version.data,
        }}

        return Response(content)


class MakeTranslationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = int(request.GET.get('translation', -1))

        translation = get_object_or_404(Translation, pk=pk)
        last_version = Version.objects.filter(translation=pk).latest('creation_date')

        serializer_translation = ReadTranslationSerializer(translation)
        serializer_version = ReadVersionSerializer(last_version)

        content = {'data': {
            'translation': serializer_translation.data,
            'last_version': serializer_version.data,
        }}

        return Response(content)


class AllVersionView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        translation = int(request.GET.get('translation', -1))

        versions = get_list_or_404(Version, translation=translation)
        serializer = AllVersionSerializer(versions, many=True)

        content = {'data': serializer.data}

        return Response(content)


class DifferencesVersionView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = int(request.GET.get('version', -1))

        current_version = get_object_or_404(Version, pk=pk)
        translation = current_version.translation
        last_version = Version.objects.filter(translation=translation).latest('creation_date')

        serializer_current = ReadVersionSerializer(current_version)
        serializer_last = ReadVersionSerializer(last_version)

        content = {'data': {
            'current_version': serializer_current.data,
            'last_version': serializer_last.data,
        }}

        return Response(content)


class OriginCommentView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        origin = int(request.GET.get('origin', 1))

        comments = get_list_or_404(CommentOrigin, origin=origin)
        serializer = OriginCommentSerializer(comments, many=True)

        content = {'data': serializer.data}

        return Response(content)
