from django.db import models

from django.contrib.auth.models import User

from file_app.models import OriginFile, OriginIcon, VersionFile


# Create your models here.
class Genre(models.Model):
    name = models.CharField('Название жанра произведения', max_length=30)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class FormatType(models.Model):
    name = models.CharField('Название формата произведения', max_length=30)

    class Meta:
        verbose_name = 'Формат произведения'
        verbose_name_plural = 'Форматы произведений'

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
    title = models.CharField('Название книги', max_length=50)
    author = models.CharField('Автор', max_length=50, blank=True, null=True)
    description = models.TextField('Описание', max_length=1500, blank=True, null=True)
    creation_date = models.DateField('Дата создания', blank=True, null=True)

    genre = models.ManyToManyField(Genre, verbose_name='Жанры', related_name='origin_set', blank=True)
    origin_language = models.ForeignKey(Language, verbose_name='Язык оригинала', related_name='origin_set',
                                        on_delete=models.SET_NULL, blank=True, null=True)
    format_type = models.ForeignKey(FormatType, verbose_name='Формат книги', related_name='origin_set',
                                    on_delete=models.SET_NULL, blank=True, null=True)

    AGES = [
        ('0', '0'),
        ('6', '6'),
        ('12', '12'),
        ('16', '16'),
        ('18', '18')
    ]
    age_limit = models.CharField('Возрастной рейтинг', max_length=2, choices=AGES, default='18')

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


class Translation(models.Model):
    creation_date = models.DateTimeField('Дата начала перевода', auto_now_add=True)

    author = models.ForeignKey(User, verbose_name='Автор', related_name='translation_set',
                               on_delete=models.SET_NULL, blank=True, null=True)
    origin = models.ForeignKey(Origin, verbose_name='Оригинал', related_name='translation_set',
                               on_delete=models.SET_NULL, blank=True, null=True)
    language = models.ForeignKey(Language, verbose_name='Язык', related_name='translation_set',
                                 on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Перевод'
        verbose_name_plural = 'Переводы'

        ordering = ['-creation_date']

    def __str__(self):
        translation_label = "Автор перевода: {}; Язык: {}; Оригинал: {}".format(self.author, self.language, self.origin)
        return translation_label


class Version(models.Model):
    creation_date = models.DateTimeField('Дата создания', auto_now_add=True)

    translation = models.ForeignKey(Translation, verbose_name='Основной перевод', related_name='version_set',
                                    on_delete=models.CASCADE)

    version_link = models.ForeignKey(VersionFile, verbose_name='Ссылка на версию', on_delete=models.CASCADE,
                                     blank=True, null=True)

    class Meta:
        verbose_name = 'Версия перевода'
        verbose_name_plural = 'Версии переводов'

        ordering = ['translation', '-creation_date']

    def __str__(self):
        translation = self.translation.__str__()
        version_label = "{} ({})".format(translation, self.creation_date)
        return version_label


class RateList(models.Model):
    rate = models.SmallIntegerField('Оценка', default=0)
    rate_date = models.DateField('Дата оценивания', auto_now_add=True)

    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='rate_set', on_delete=models.CASCADE)
    translation = models.ForeignKey(Translation, verbose_name='Перевод', related_name='rate_set',
                                    on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

        ordering = ['translation']

    def __str__(self):
        translation = self.translation.__str__()
        rate_label = "Пользователь {} поставил{} переводу: {}".format(self.user.username, self.rate, translation)
        return rate_label


class Comment(models.Model):
    post = models.TextField('Текст комментария', max_length=1000)
    post_date = models.DateTimeField('Дата создания', auto_now_add=True)

    author = models.ForeignKey(User, verbose_name='Автор', related_name="%(class)s_set",
                               on_delete=models.SET_NULL, blank=True, null=True)
    parent_comment = models.ForeignKey('self', verbose_name='Родительский коментарий',
                                       related_name="%(class)s_child_set",
                                       on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True


class CommentOrigin(Comment):
    origin = models.ForeignKey(Origin, verbose_name='Книга', related_name="comment_origin_set",
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий произведения'
        verbose_name_plural = 'Комментарии произведений'

        ordering = ['-post_date', 'origin']

    def __str__(self):
        comment = "{}: {}...".format(self.author.username, self.post[:20])
        origin = self.origin.__str__()
        return "({}) {}".format(comment, origin)
