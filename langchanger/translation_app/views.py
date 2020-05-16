from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Q, Sum, F, Value, IntegerField
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import ListAPIView

from .models import *
from .serializers import *
from registration_app.serializers import RateUserSerializer

from file_app.serializers import VersionFileSerializer
from file_app.models import VersionFile
from file_app.bot import send_file


def paginator(request, queryset):
    page_size = int(request.GET.get('page_size', 6))
    current_page = int(request.GET.get('current_page', 1))

    first_item = (current_page - 1) * page_size
    last_item = current_page * page_size

    queryset_part = queryset[first_item:last_item]

    return queryset_part


class FormatTypeListView(ListAPIView):
    queryset = FormatType.objects.all()
    serializer_class = FormatTypeSerializer
    permission_classes = [permissions.AllowAny]


class GenreListView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]


class LanguageListView(ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.AllowAny]


class MainPageView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        last_origins = Origin.objects.all()
        serializer = AllOriginSerializer(last_origins, many=True)

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
            if key in self.filter_name_set:
                filter_key = self.filter_name_set[key]
                complete_filter[filter_key] = data

        queryset = Origin.objects.filter(**complete_filter)

        if order_by == 'relevance':
            queryset = queryset.annotate(rate=Sum('translation_set__rate_set__rate'))

            queryset_not_null = queryset.filter(rate__isnull=False)
            queryset_null = queryset.filter(rate__isnull=True).annotate(rate=Value(0, IntegerField()))
            queryset = queryset_not_null.union(queryset_null)

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

        language_set = set(Translation.objects.filter(origin=pk).values_list('language'))
        language_set = [x[0] for x in language_set]
        languages = Language.objects.filter(pk__in=language_set)

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

        translations = Translation.objects.filter(
            Q(origin=origin) &
            Q(language=language)
        )

        if not translations:
            return Response(status=400)

        serializer = TranslationByLanguageSerializer(translations, many=True)

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

        translations = Translation.objects.filter(pk=pk).annotate(rate=Sum('rate_set__rate'))

        if not translations:
            return Response(status=400)

        translation = translations.first()
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

    def post(self, request):
        data = request.data.copy()
        data['author'] = request.user.id

        serializer_translation = MakeTranslationSerializer(data=data)
        serializer_file = VersionFileSerializer(data=data)

        check_set = (
            serializer_translation.is_valid(),
            serializer_file.is_valid(),
        )

        if False not in check_set:
            translation = serializer_translation.save()

            tg_hash = send_file(document=request.data['file'].open(), chat='VersionFile')
            file = serializer_file.save(tg_hash=tg_hash)

            Version.objects.create(translation=translation, version_link=file)

            return Response(status=200)

        return Response(
            {'translation_errors': serializer_translation.errors,
             'file_errors': serializer_file.errors},
            status=400)

    def put(self, request):
        translation_id = int(request.POST.get('translation', -1))

        translation = get_object_or_404(Translation, pk=translation_id)

        serializer_file = VersionFileSerializer(data=request.data)

        if request.user.id == translation.author.id:
            if serializer_file.is_valid():
                tg_hash = send_file(document=request.data['file'].open(), chat='VersionFile')
                file = serializer_file.save(tg_hash=tg_hash)

                Version.objects.create(translation=translation, version_link=file)

                return Response(status=200)
            return Response(serializer_version.errors, status=400)
        return Response({'errors': 'user is not author of translation'}, status=400)

    def delete(self, request):
        pk = int(request.POST.get('translation', -1))

        translation = get_object_or_404(Translation, pk=pk)
        file_id_set = Version.objects.filter(translation=translation.id).values('version_link')

        if request.user.id == translation.author.id:
            VersionFile.objects.filter(id__in=file_id_set).delete()
            translation.delete()

            return Response(status=200)
        return Response({'error': 'This user is not author of translation'}, status=400)


class AllVersionView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        translation = int(request.GET.get('translation', -1))

        versions = get_list_or_404(Version, translation=translation)
        serializer = AllVersionSerializer(versions, many=True)

        content = {'data': serializer.data}

        return Response(content)


class DeleteVersionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    renderer_classes = [JSONRenderer]

    def delete(self, request):
        pk = int(request.POST.get('version', -1))

        version = get_object_or_404(Version, pk=pk)
        file = VersionFile.objects.get(id=version.version_link.id)
        translation = Translation.objects.get(pk=version.translation.id)

        if translation.author.id == request.user.id:
            file.delete()
            return Response(status=200)
        return Response({'error': 'This user is not author of translation'}, status=400)


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
        origin = int(request.GET.get('origin', -1))

        comments = get_list_or_404(CommentOrigin, origin=origin)
        serializer = OriginCommentSerializer(comments, many=True)

        content = {'data': serializer.data}

        return Response(content)


class MakeOriginCommentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    renderer_classes = [JSONRenderer]

    def post(self, request):
        comment_serializer = MakeOriginCommentSerializer(data=request.data)

        if comment_serializer.is_valid():
            comment_serializer.save()

            return Response(status=200)
        return Response(comment_serializer.errors, status=400)


class MakeRateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    renderer_classes = [JSONRenderer]

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id

        rate_list = RateList.objects.filter(Q(user=data['user']) & Q(translation=data['translation']))

        if rate_list:
            rate = rate_list.first()
            rate_serializer = MakeRateSerializer(rate, data=data)
        else:
            rate_serializer = MakeRateSerializer(data=data)

        if rate_serializer.is_valid():
            rate_serializer.save()

            return Response(status=200)
        return Response(rate_serializer.errors, status=400)

    def delete(self, request):
        user = request.user.id
        translation = int(request.POST.get('translation', -1))

        rate_list = RateList.objects.filter(Q(user=user) & Q(translation=translation))

        if rate_list:
            rate = rate_list.first()
            rate.delete()

            return Response(status=200)
        return Response({
            'errors': "Request rate doesn't exist"
        }, status=400)

