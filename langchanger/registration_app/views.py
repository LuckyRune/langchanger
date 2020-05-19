from django.shortcuts import get_object_or_404
from django.db.models import Count, Sum, Value, IntegerField

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer

from .models import *
from .serializers import *

from translation_app.models import Translation
from translation_app.serializers import AllTranslationSerializer, AllOriginSerializer

from file_app.serializers import UserIconSerializer
from file_app.models import UserIcon
from file_app.bot import send_image


def paginator(request, queryset):
    page_size = int(request.GET.get('page_size', 6))
    current_page = int(request.GET.get('current_page', 1))

    first_item = (current_page - 1) * page_size
    last_item = current_page * page_size

    queryset_part = queryset[first_item:last_item]

    return queryset_part


class AllUserView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    ordering_set = {
        'rate': '-rate',
        'achievement': '-count_achievement',
        'translation': '-count_translation',
    }

    def get(self, request):
        order_by = request.GET.get('order', 'rate')

        queryset = User.objects.filter(is_staff=False)
        queryset = queryset.annotate(count_achievement=Count('user_profile__achievements'))
        queryset = queryset.annotate(count_translation=Count('translation_set'))
        queryset = queryset.annotate(rate=Sum('translation_set__rate_set__rate'))

        queryset_not_null = queryset.filter(rate__isnull=False)
        queryset_null = queryset.filter(rate__isnull=True).annotate(rate=Value(0, IntegerField()))
        queryset = queryset_not_null.union(queryset_null)

        if order_by in self.ordering_set:
            queryset = queryset.order_by(self.ordering_set[order_by])

        response_queryset = paginator(request, queryset)

        serializer = AllUserSerializer(response_queryset, many=True)

        content = {'data': serializer.data}

        return Response(content)


class MainUserInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = request.user.id

        user = User.objects.get(pk=pk)

        user_serializer = RateUserSerializer(user)

        return Response(user_serializer.data, status=200)


class ProfileUserView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = int(request.GET.get('user', -1))

        users = User.objects.filter(pk=pk).annotate(rate=Sum('translation_set__rate_set__rate'))

        if not users:
            return Response(status=400)

        user = users.first()
        translations = Translation.objects.filter(author=pk).annotate(rate=Sum('rate_set__rate'))

        serializer_translations = AllTranslationSerializer(translations, many=True)
        serializer_user = DetailedUserSerializer(user)

        content = {'data': {
            'user': serializer_user.data,
            'translations': serializer_translations.data,
        }}

        return Response(content, status=200)


class AchievementView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = int(request.GET.get('achievement', -1))

        achievement = get_object_or_404(Achievement, pk=pk)

        serializer = AchievementSerializer(achievement)

        content = {'data': serializer.data}

        return Response(content)


class OnHoldUserView(APIView):
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
        user = int(request.GET.get('user', -1))

        origin_list = get_object_or_404(UserProfile, user=user).on_hold

        complete_filter = {}
        for key, data in raw_filter.items():
            if key in self.filter_name_set:
                filter_key = self.filter_name_set[key]
                complete_filter[filter_key] = data

        queryset = origin_list.filter(**complete_filter)

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


class SettingUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user.id)

        serializer_user = SettingUserSerializer(user)
        serializer_profile = PostUserProfileSerializer(profile)

        content = {'data': {
            'main': serializer_user.data,
            'additional': serializer_profile.data
        }}

        return Response(content)

    def put(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user.id)
        profile_icon = UserIcon.objects.get(id=profile.profile_icon.id)

        serializer_user = SettingUserSerializer(user, data=request.data)
        serializer_profile = PostUserProfileSerializer(profile, data=request.data)

        check_set = (serializer_user.is_valid(), serializer_profile.is_valid())

        if False not in check_set:
            serializer_user.save()

            if request.data.get('image', False):
                serializer_profile_icon = UserIconSerializer(profile_icon, data=request.data)

                if serializer_profile_icon.is_valid():
                    tg_hash = send_image(image=request.data['image'].open(), chat='UserIcon')
                    icon = serializer_profile_icon.save(tg_hash=tg_hash)

                    serializer_profile.save(profile_icon=icon)
                else:
                    return Response({
                        'image_errors': serializer_profile_icon.errors
                    }, status=400)
            else:
                serializer_profile.save()

            return Response(status=200)

        return Response({
            'main_errors': serializer_user.errors,
            'profile_errors': serializer_profile.errors
        }, status=400)

    def delete(self, request):
        user = User.objects.get(id=request.user.id)
        profile = UserProfile.objects.get(user=user.id)

        if profile.profile_icon:
            profile_icon = UserIcon.objects.get(id=profile.profile_icon.id)
            profile_icon.delete()

        user.delete()
        return Response(status=200)


class RegisterUserView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def post(self, request):
        serializer_user = RegisterUserSerializer(data=request.data)
        serializer_profile = PostUserProfileSerializer(data=request.data)

        check_set = (serializer_user.is_valid(), serializer_profile.is_valid())

        if False not in check_set:

            if request.data.get('image', False):
                serializer_profile_icon = UserIconSerializer(data=request.data)

                if serializer_profile_icon.is_valid():
                    tg_hash = send_image(image=request.data['image'].open(), chat='UserIcon')
                    icon = serializer_profile_icon.save(tg_hash=tg_hash)
                else:
                    return Response({
                        'image_errors': serializer_profile_icon.errors
                    }, status=400)

                user = serializer_user.save()
                serializer_profile.save(user=user, profile_icon=icon)
            else:
                user = serializer_user.save()
                serializer_profile.save(user=user)

            return Response(status=200)

        return Response({
            'main_errors': serializer_user.errors,
            'profile_errors': serializer_profile.errors
        }, status=400)
