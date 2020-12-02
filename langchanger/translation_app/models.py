import datetime

from django.contrib.auth.models import User
from django.db import models

from file_app.models import OriginFile, OriginIcon


# Create your models here.
class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=30)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField('Язык', max_length=30)

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.name


class Origin(models.Model):
    title = models.CharField('Название произведения', max_length=50)
    author = models.CharField('Автор', max_length=50, blank=True, null=True)
    description = models.TextField('Описание', max_length=1500, blank=True,
                                   null=True)

    publication_date = models.DateTimeField('Дата создания',
                                            default=datetime.datetime.now)
    creation_date = models.DateField('Дата создания', blank=True, null=True)

    genre = models.ManyToManyField(Genre, verbose_name='Жанры',
                                   related_name='origin_set', blank=True)
    origin_language = models.ForeignKey(Language,
                                        verbose_name='Язык оригинала',
                                        related_name='origin_set',
                                        on_delete=models.SET_NULL, blank=True,
                                        null=True)

    AGES = [
        ('0', '0'),
        ('6', '6'),
        ('12', '12'),
        ('16', '16'),
        ('18', '18')
    ]
    age_limit = models.CharField('Возрастной рейтинг', max_length=2,
                                 choices=AGES, default='18')

    poster = models.ForeignKey(OriginIcon, verbose_name='Постер произведения', on_delete=models.SET_NULL,
                               blank=True, null=True)
    source_link = models.ForeignKey(OriginFile, verbose_name='Ссылка на произведение', on_delete=models.SET_NULL,
                                    blank=True, null=True)

    class Meta:
        verbose_name = 'Оригинал'
        verbose_name_plural = 'Оригиналы'

        ordering = ['id']

    def __str__(self):
        origin_label = "{}, {}".format(self.title, self.author)
        return origin_label


class Comment(models.Model):
    post = models.TextField('Текст комментария', max_length=1000)
    post_date = models.DateTimeField('Дата создания',
                                     default=datetime.datetime.now)

    author = models.ForeignKey(User, verbose_name='Автор',
                               related_name="%(class)s_set",
                               on_delete=models.SET_NULL, blank=True,
                               null=True)
    parent_comment = models.ForeignKey('self',
                                       verbose_name='Родительский коментарий',
                                       related_name="%(class)s_child_set",
                                       on_delete=models.CASCADE, null=True,
                                       blank=True)

    class Meta:
        abstract = True


class CommentOrigin(Comment):
    origin = models.ForeignKey(Origin, verbose_name='Оригинал', related_name="comment_origin_set",
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий оригинала'
        verbose_name_plural = 'Комментарии оригиналов'

        ordering = ['-post_date', 'origin']

    def __str__(self):
        comment = "{}: {}...".format(self.author.username, self.post[:20])
        origin = self.origin.__str__()
        return "({}) {}".format(comment, origin)
