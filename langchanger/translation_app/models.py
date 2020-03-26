from django.db import models

from django.contrib.auth.models import User


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
    isbn = models.CharField('ISBN', max_length=13)
    title = models.CharField('Название книги', max_length=50)
    author = models.CharField('Автор', max_length=50, blank=True, null=True)
    description = models.TextField('Описание', max_length=1500, blank=True, null=True)
    creation_date = models.DateField('Дата создания', blank=True, null=True)

    genre = models.ManyToManyField(Genre, verbose_name='Жанры', blank=True)
    origin_language = models.ForeignKey(Language, verbose_name='Язык оригинала', on_delete=models.SET_NULL,
                                        blank=True, null=True)
    format_type = models.ForeignKey(FormatType, verbose_name='Формат книги', on_delete=models.SET_NULL,
                                    blank=True, null=True)

    AGES = [
        ('0', '0'),
        ('6', '6'),
        ('12', '12'),
        ('16', '16'),
        ('18', '18')
    ]
    age_limit = models.CharField('Возрастной рейтинг', max_length=2, choices=AGES, default=AGES[-1])

    poster_hash = models.CharField('Хеш постера', max_length=120, blank=True, null=True)
    poster = models.ImageField('Постер произведения', upload_to='images/', blank=True, null=True)
    source_hash = models.CharField('Хеш произведения', max_length=120, blank=True, null=True)
    source_link = models.FileField('Ссылка на произведение', upload_to='files/', blank=True, null=True)

    class Meta:
        verbose_name = 'Оригинал'
        verbose_name_plural = 'Оригиналы'

        ordering = ['id']

    def __str__(self):
        origin_label = "{}, {}".format(self.title, self.author)
        return origin_label


class Translation(models.Model):
    creation_date = models.DateTimeField('Дата начала перевода', auto_now_add=True)
    rate = models.BigIntegerField('Оценка', default=0)

    author = models.ForeignKey(User, verbose_name='Автор', default=2, on_delete=models.SET_DEFAULT)
    origin = models.ForeignKey(Origin, verbose_name='Оригинал', on_delete=models.SET_NULL, blank=True, null=True)
    language = models.ForeignKey(Language, verbose_name='Язык', on_delete=models.SET_NULL, blank=True, null=True)

    translation_hash = models.CharField('Хеш перевода', max_length=120, blank=True, null=True)
    translation_link = models.FileField('Ссылка на перевод', upload_to='files/', blank=True, null=True)

    class Meta:
        verbose_name = 'Перевод'
        verbose_name_plural = 'Переводы'

        ordering = ['-creation_date']

    def __str__(self):
        translation_label = "Автор перевода: {}; Язык: {}; Оригинал: {}".format(self.author, self.language, self.origin)
        return translation_label

    def change_translation_link(self, version):
        pass


class Version(models.Model):
    change_number = models.PositiveIntegerField('Число изменений', default=0)
    creation_date = models.DateTimeField('Дата создания', auto_now_add=True)

    translation = models.ForeignKey(Translation, verbose_name='Основной перевод', on_delete=models.CASCADE)

    version_hash = models.CharField('Хеш версии', max_length=120, blank=True, null=True)
    version_link = models.FileField('Ссылка на версию', upload_to='files/', blank=True, null=True)

    class Meta:
        verbose_name = 'Версия перевода'
        verbose_name_plural = 'Версии переводов'

        ordering = ['translation', '-creation_date']

    def __str__(self):
        translation = self.translation.__str__()
        version_label = "{} № {} ({})".format(translation, self.change_number, self.creation_date)
        return version_label


class RateList(models.Model):
    rate = models.SmallIntegerField('Оценка', default=0)

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    translation = models.ForeignKey(Translation, verbose_name='Перевод', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

        ordering = ['translation']

    def __str__(self):
        translation = self.translation.__str__()
        rate_label = "Пользователь {} поставил{} переводу: {}".format(self.user.username, self.rate, translation)
        return rate_label

    def add_rate(self):
        pass

    def change_rate(self):
        pass

    def delete_rate(self):
        pass


class Comment(models.Model):
    post = models.TextField('Текст комментария', max_length=1000)
    post_date = models.DateTimeField('Дата создания', auto_now_add=True)

    author = models.ForeignKey(User, verbose_name='Автор', default=2, on_delete=models.SET_DEFAULT)
    parent_comment = models.ForeignKey('Comment', verbose_name='Родительский коментарий', on_delete=models.CASCADE,
                                       null=True, blank=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

        ordering = ['-post_date']

    def __str__(self):
        comment_label = "{}: {}...".format(self.author.username, self.post[:20])
        return comment_label


class CommentOrigin(models.Model):
    comment = models.OneToOneField(Comment, verbose_name='Основной комментарий', on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, verbose_name='Книга', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий произведения'
        verbose_name_plural = 'Комментарии произведений'

        ordering = ['origin']

    def __str__(self):
        comment = self.comment.__str__()
        origin = self.origin.__str__()
        return "{} ({})".format(comment, origin)
