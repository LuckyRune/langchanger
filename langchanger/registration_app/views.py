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

    ordering_set = {
        'rate': 'user_profile__rate',
        'achievement': 'ach',
        'translation': '',
    }

    def get(self, request):
        order_by = request.GET.get('order', 'rate')

        if order_by is None:
            queryset = User.objects.filter(is_staff=False)
        else:
            # queryset = User.objects.filter(is_staff=False).order_by(self.ordering_set[order_by])
            queryset = User.objects.filter(is_staff=False).order_by('rate')

        response_queryset = paginator(request, queryset)

        serializer = DetailedUserSerializer(response_queryset, many=True)

        content = {'data': serializer.data}
        for user in content['data']:
            user['count_achievement'] = len(user['user_profile']['achievements'])
            count_translation = Translation.objects.filter(author=user['id']).count()
            user['count_translation'] = count_translation

        return Response(content)


class ProfileUserView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = int(request.GET.get('user', 3))

        user = get_object_or_404(User, pk=pk)
        translations = Translation.objects.filter(author=pk)

        serializer_translations = UserProfileTranslationSerializer(translations, many=True)
        serializer_user = DetailedUserSerializer(user)

        content = {'data': {
            'user': serializer_user.data,
            'translations': serializer_translations.data,
        }}

        return Response(content)


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

    def get(self, request):
        pk = int(request.GET.get('origin', -1))

        origin = get_object_or_404(Origin, pk=pk)

        serializer = MainInfoOriginSerializer(origin)

        content = {'data': serializer.data}

        return Response(content)


class SettingUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = int(request.GET.get('user', 3))

        user = get_object_or_404(User, pk=pk)

        serializer = SettingUserSerializer(user)

        content = {'data': serializer.data}

        return Response(content)
