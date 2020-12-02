from django.contrib.auth.models import User
from django.db import models

from file_app.models import UserIcon
from translation_app.models import Origin


# Create your models here.
class UserProfile(models.Model):

    description = models.TextField('О себе', max_length=1000, blank=True, null=True)
    ip = models.CharField('IP', max_length=25, null=True, blank=True)

    user = models.OneToOneField(User, related_name='user_profile',
                                verbose_name='Основной пользователь', on_delete=models.CASCADE)
    on_hold = models.ManyToManyField(Origin, verbose_name='Отложенное', related_name='user_profile_set', blank=True)

    profile_icon = models.ForeignKey(UserIcon, verbose_name='Аватарка', on_delete=models.SET_NULL,
                                     blank=True, null=True)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return self.user.username


class Blacklist(models.Model):
    ip = models.CharField('IP', max_length=25, null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Забаненый пользователь'
        verbose_name_plural = 'Чёрный список'

    def __str__(self):
        blacklist_label = "{} - забанен".format(self.user.username)
        return blacklist_label


