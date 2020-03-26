from django.db import models

from django.contrib.auth.models import User

from translation_app.models import Origin


# Create your models here.
class UserProfile(models.Model):

    rate = models.BigIntegerField('Общая оценка пользователя', default=0)
    description = models.TextField('О себе', max_length=1000, blank=True, null=True)

    user = models.OneToOneField(User, verbose_name='Основной пользователь', on_delete=models.CASCADE)
    achievements = models.ManyToManyField('Achievement', verbose_name='Достижения', blank=True)
    on_hold = models.ManyToManyField(Origin, verbose_name='Отложенное', blank=True)

    profile_icon_hash = models.CharField('Хеш аватарки', max_length=120, blank=True, null=True)
    profile_icon = models.ImageField('Аватарка', upload_to='images/', blank=True, null=True)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

        ordering = ['rate']

    def __str__(self):
        user_label = "{} ({})".format(self.user.username, self.rate)
        return user_label


class Achievement(models.Model):
    name = models.CharField('Название', max_length=30)
    description = models.TextField('Описание', max_length=500, blank=True, null=True)
    rate = models.IntegerField('Стоимость', default=1)

    icon_hash = models.CharField('Хеш иконки', max_length=120, blank=True, null=True)
    icon = models.ImageField('Иконка', upload_to='images/', blank=True, null=True)

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'

        ordering = ['name']

    def __str__(self):
        return self.name

    def add_rate(self, user: UserProfile):
        user.rate += self.rate

