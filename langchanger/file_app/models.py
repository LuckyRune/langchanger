from django.db import models


class TgFile(models.Model):
    file = models.FileField('Файл', upload_to='files')
    tg_hash = models.CharField('Хеш файла', max_length=120, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        text = 'Класс {0}, хеш: {1}'.format(self.__class__.__name__, self.tg_hash)
        return text


class TgImage(models.Model):
    image = models.ImageField('Изображение', upload_to='images')
    tg_hash = models.CharField('Хеш изображения', max_length=120, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        text = 'Класс {0}, хеш: {1}'.format(self.__class__.__name__, self.tg_hash)
        return text


class UserIcon(TgImage):

    class Meta:
        verbose_name_plural = 'Аватарки пользователей'
        verbose_name = 'Аватарка пользователя'


class OriginIcon(TgImage):

    class Meta:
        verbose_name_plural = 'Иконки оригиналов'
        verbose_name = 'Иконка оригинала'


class AchievementIcon(TgImage):

    class Meta:
        verbose_name_plural = 'Иконки достижений'
        verbose_name = 'Иконка достижения'


class VersionFile(TgFile):

    class Meta:
        verbose_name_plural = 'Файлы версий переводов'
        verbose_name = 'Файл версии перевода'


class OriginFile(TgFile):

    class Meta:
        verbose_name_plural = 'Файлы оригионалов'
        verbose_name = 'Файл оригинала'
