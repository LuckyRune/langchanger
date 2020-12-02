from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from file_app.bot import send_image
from translation_app.serializers import AllOriginSerializer
from .permissions import *
from .serializers import *


def paginator(request, queryset):
    page_size = int(request.GET.get('page_size', 6))
    current_page = int(request.GET.get('current_page', 1))

    first_item = (current_page - 1) * page_size
    last_item = current_page * page_size

    queryset_part = queryset[first_item:last_item]

    return queryset_part


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AllUserView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        search_sentence = request.GET.get('sentence')

        queryset = User.objects.filter(is_staff=False)

        if search_sentence:
            queryset = queryset.filter(username__icontains=search_sentence)

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
        group_serializer = GroupSerializer(user.groups, many=True)

        return Response({
            'main': user_serializer.data,
            'groups': group_serializer.data
        }, status=200)


class ProfileUserView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = int(request.GET.get('user', -1))

        if not users:
            return Response(status=400)

        user = users.first()

        serializer_user = DetailedUserSerializer(user)

        content = {'data': {
            'user': serializer_user.data,
        }}

        return Response(content, status=200)


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
        ip = get_client_ip(request)

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
                serializer_profile.save(user=user, profile_icon=icon, ip=ip)
            else:
                user = serializer_user.save()
                serializer_profile.save(user=user, ip=ip)

            return Response(status=200)

        return Response({
            'main_errors': serializer_user.errors,
            'profile_errors': serializer_profile.errors
        }, status=400)


class OnHoldUserView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    filter_name_set = {
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
            queryset = queryset.order_by('id')

        response_queryset = paginator(request, queryset)

        serializer = AllOriginSerializer(response_queryset, many=True)

        content = {'data': serializer.data}

        return Response(content)


class ChangeOnHoldUserView(APIView):
    permission_classes = [permissions.IsAuthenticated, BlacklistPermission]

    renderer_classes = [JSONRenderer]

    def put(self, request):
        user = request.user.id
        origin = int(request.POST.get('origin', -1))

        profile = UserProfile.objects.get(user=user)
        origin = get_object_or_404(Origin, id=origin)

        profile.on_hold.add(origin)

        profile.save()

        serializer = UserProfileSerializer(profile)

        return Response(serializer.data, status=200)

    def delete(self, request):
        user = request.user.id

        origin = int(request.POST.get('origin', -1))

        profile = UserProfile.objects.get(user=user)
        origin = get_object_or_404(Origin, id=origin)

        profile.on_hold.remove(origin)

        profile.save()

        serializer = UserProfileSerializer(profile)

        return Response(serializer.data, status=200)


class BanUserView(APIView):
    permission_classes = [ModeratorPermission]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        queryset = Blacklist.objects.all()

        response_queryset = paginator(request, queryset)

        serializer = BlacklistSerializer(response_queryset, many=True)

        return Response(serializer.data, status=200)

    def post(self, request):
        user_id = int(request.POST.get('user', -1))
        serializer_banned_user = PostBlacklistSerializer(data=request.data)

        if serializer_banned_user.is_valid():
            serializer_banned_user.save()

            return Response(status=200)
        return Response(status=400)

    def delete(self, request):
        user_id = int(request.POST.get('user', -1))

        banned_user = get_object_or_404(Blacklist, user=user_id)
        banned_user.delete()

        return Response(status=200)


class BanUserIPView(APIView):
    permission_classes = [ModeratorPermission]

    renderer_classes = [JSONRenderer]

    def post(self, request):
        user_id = int(request.POST.get('user', -1))

        banned_user = get_object_or_404(Blacklist, user=user_id)
        user_profile = get_object_or_404(UserProfile, user__id=user_id)

        banned_user.ip = user_profile.ip
        banned_user.save()

        return Response(status=200)
