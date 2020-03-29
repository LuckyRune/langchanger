from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer

from .models import *
from .serializers import *
from . import __package__ as app


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

    def get(self, request):
        filter_dict = request.GET.get('filters', None)

        if filter_dict is None:
            queryset = Origin.objects.all()
        else:
            queryset = Origin.objects.filter(
                format_type__name__in=filter_dict['format_type'],
                genre__name__in=filter_dict['genre'],
                age_limit__in=filter_dict['age_limit'])

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
        serializer_origin = OneOriginSerializer(origin, many=True)

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
        language = request.GET.get('language', None)

        if origin != -1 and language is not None:
            translations = Translation.objects.filter(
                Q(origin=origin) &
                Q(language__name=language)
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
        serializer = ReadOriginSerializer(origin, many=True)

        content = {'data': serializer.data}

        return Response(content)


class ReadTranslationView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = int(request.GET.get('translation', -1))

        translation = get_object_or_404(Translation, pk=pk)
        last_version = get_list_or_404(Version, translation=pk).objects.latest('creation_date')

        serializer_translation = ReadTranslationSerializer(translation)
        serializer_version = ReadVersionSerializer(last_version)

        content = {'data': {
            'translation': serializer_translation.data,
            'last_version': serializer_version,
        }}

        return Response(content)


class MakeTranslationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = int(request.GET.get('translation', -1))

        if pk != -1:
            translation = Translation.objects.get(pk=pk)
            last_version = Version.objects.filter(translation=pk).latest('creation_date')

            serializer_translation = ReadTranslationSerializer(translation)
            serializer_version = ReadVersionSerializer(last_version)

            content = {'data': {
                'translation': serializer_translation.data,
                'last_version': serializer_version,
            }}
        else:
            content = {'data': 'None'}

        return Response(content)


class AllVersionView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        translation = int(request.GET.get('translation', -1))

        versions = get_list_or_404(Origin, translation=translation)
        serializer = AllVersionSerializer(versions, many=True)

        content = {'data':  serializer.data}

        return Response(content)


class DifferenceVersionView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = int(request.GET.get('version', -1))

        current_version = get_object_or_404(Version, pk=pk)
        translation = current_version.translation
        last_version = Version.objects.filter(translation=translation).latest('creation_date')

        serializer_current = ReadVersionSerializer(current_version, many=True)
        serializer_last = ReadVersionSerializer(last_version, many=True)

        content = {'data': {
            'current_version': serializer_current.data,
            'last_version': serializer_last.data,
        }}

        return Response(content)
