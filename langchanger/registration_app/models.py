from django.db import models

from django.contrib.auth.models import User

from translation_app.models import Origin


# Create your models here.
class UserProfile(models.Model):

    rate = models.BigIntegerField('Общая оценка пользователя', )
    description = models.TextField('О себе', max_length=1000)

    user = models.OneToOneField(User, verbose_name='Основной пользователь', on_delete=models.CASCADE)
    achievements = models.ManyToManyField('Achievement', verbose_name='Достижения', blank=True, null=True)
    on_hold = models.ManyToManyField(Origin, verbose_name='Отложенное', blank=True, null=True)

    profile_icon = models.ImageField('Аватарка', )


class Achievement(models.Model):
    name = models.TextField('Название', max_length=30)
    description = models.TextField('Описание', max_length=500)
    rate = models.IntegerField('Стоимость', )

    def add_rate(self, user: UserProfile):
        user.rate += self.rate
