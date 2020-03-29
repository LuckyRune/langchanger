from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer

from .models import *
from .serializers import *
from translation_app.models import Translation, Origin
from translation_app.serializers import UserProfileTranslationSerializer, MainInfoOriginSerializer


def paginator(request, queryset):
    page_size = int(request.GET.get('page_size', 3))
    current_page = int(request.GET.get('current_page', 1))

    first_item = (current_page - 1) * page_size
    last_item = current_page * page_size

    queryset_part = queryset[first_item:last_item]

    return queryset_part


class AllUserView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        queryset = UserProfile.objects.all()

        response_queryset = paginator(request, queryset)

        serializer = AllUserProfileSerializer(response_queryset, many=True)
        for user in serializer:
            user['field'] = '+'

        content = {'data': serializer.data}

        return Response(content)


class ProfileUserView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = int(request.GET.get('user', -1))

        user = get_object_or_404(UserProfile, pk=pk)
        translations = Translation.objects.filter(user=pk)

        serializer_translations = UserProfileTranslationSerializer(translations, many=True)
        serializer_user = UserProfileSerializer(user)

        content = {'data': {
            'user': serializer_user.data,
            'translations': serializer_translations.data,
        }}

        return Response(content)


class AchievementUserView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        user = int(request.GET.get('user', -1))

        achievements_id = get_object_or_404(UserProfile, pk=user).objects.values('achievements')
        achievements_object = Achievement.objects.filter(id__in=achievements_id)

        serializer = AchievementSerializer(achievements_object, many=True)

        content = {'data': serializer.data}

        return Response(content)


class HoldOnUserView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        user = int(request.GET.get('user', -1))

        origins_id = get_object_or_404(UserProfile, pk=user).objects.values('hold_on')
        origins_object = Origin.objects.filter(id__in=origins_id)

        serializer = MainInfoOriginSerializer(origins_object, many=True)

        content = {'data': serializer.data}

        return Response(content)


class SettingUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = int(request.GET.get('user', -1))

        user = get_object_or_404(UserProfile, pk=pk)

        serializer = SettingUserSerializer(user, many=True)

        content = {'data': serializer.data}

        return Response(content)
