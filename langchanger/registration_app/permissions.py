from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework import permissions

from .models import Blacklist


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class ModeratorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user_id = request.user.id
        user = User.objects.get(pk=user_id)

        is_moderator = get_object_or_404(User, pk=user_id).groups.filter(name__icontains='Moderator')

        if is_moderator or user.is_staff:
            return True
        return False


class BlacklistPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user_ip = get_client_ip(request)

        check = Blacklist.objects.filter(Q(ip=user_ip) | Q(user__id=request.user.id))

        if check:
            return False

        return True


