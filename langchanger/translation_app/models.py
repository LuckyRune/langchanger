from django.db import models

from registration_app.models import UserProfile


# Create your models here.
class Genre(models.Model):
    name = models.TextField('Название жанра книги', max_length=30)


class FormatType(models.Model):
    name = models.TextField('Название формата книги', max_length=30)


class Language(models.Model):
    name = models.TextField('Язык', max_length=30)


class Origin(models.Model):
    isbn = models.TextField('ISBN', max_length=13)
    title = models.TextField('Название книги', max_length=50)
    author = models.TextField('Автор', max_length=50)
    description = models.TextField('Описание', max_length=1500)
    creation_date = models.DateField('Дата создания', blank=True, null=True)

    genre = models.ManyToManyField(Genre, verbose_name='Жанры', blank=True, null=True)
    origin_language = models.ForeignKey(Language, verbose_name='Язык оригинала', on_delete=models.SET_NULL,
                                        blank=True, null=True
                                        )
    format_type = models.ForeignKey(FormatType, verbose_name='Формат книги', on_delete=models.SET_NULL,
                                    blank=True, null=True
                                    )

    AGES = ['0', '6', '12', '16', '18']
    age_limit = models.TextField('Возрастной рейтинг', max_length=2, choices=AGES, default=AGES[-1])

    poster = models.ImageField('Постер книги',)
    source_link = models.FileField('Ссылка на книгу',)


class Translation(models.Model):
    creation_date = models.DateTimeField('Дата начала перевода', auto_now_add=True)
    rate = models.BigIntegerField('Оценка',)

    author = models.ForeignKey(UserProfile, verbose_name='Автор', default='anonymous', on_delete=models.SET_DEFAULT)
    origin = models.ForeignKey(Origin, verbose_name='Оригинал', on_delete=models.SET_NULL, blank=True, null=True)
    language = models.ForeignKey(Language, verbose_name='Язык', on_delete=models.SET_NULL, blank=True, null=True)

    translation_link = models.FileField('Ссылка на перевод',)

    def change_translation_link(self, version):
        pass


class Version(models.Model):
    creation_date = models.DateTimeField('Дата создания', auto_now_add=True)

    translation = models.ForeignKey(Translation, verbose_name='Основной перевод', on_delete=models.CASCADE)

    version_link = models.FileField('Ссылка на версию', )


class RateList(models.Model):
    rate = models.SmallIntegerField('Оценка', )

    user = models.ForeignKey(UserProfile, verbose_name='Пользователь', on_delete=models.CASCADE)
    translation = models.ForeignKey(Translation, verbose_name='Перевод', on_delete=models.CASCADE)

    def add_rate(self):
        pass

    def change_rate(self):
        pass

    def delete_rate(self):
        pass


class Comment(models.Model):
    post = models.TextField('Текст комментария', max_length=1000)
    post_date = models.DateTimeField('Дата создания', auto_now_add=True)

    author = models.ForeignKey(UserProfile, verbose_name='Автор', default='anonymous', on_delete=models.SET_DEFAULT)
    parent_comment = models.ForeignKey('Comment', verbose_name='Родительский коментарий', on_delete=models.CASCADE,
                                       null=True, blank=True
                                       )


class CommentOrigin(models.Model):
    comment = models.OneToOneField(Comment, verbose_name='Основной комментарий', on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, verbose_name='Книга', on_delete=models.CASCADE)
