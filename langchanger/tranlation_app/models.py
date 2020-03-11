from django.db import models

from registration_app.models import UserProfile


# Create your models here.
class Genre(models.Model):
    name = models.TextField()


class FormatType(models.Model):
    name = models.TextField()


class Language(models.Model):
    name = models.TextField()


class Origin(models.Model):
    isbn = models.TextField()
    title = models.TextField()
    author = models.TextField()
    description = models.TextField()
    creation_date = models.DateField()

    genre = models.ManyToManyField(Genre, blank=True, null=True)
    format_type = models.ForeignKey(FormatType, on_delete=models.SET_NULL, blank=True, null=True)

    AGES = ['0', '6', '12', '16', '18']
    age_limit = models.TextField(choices=AGES, default=AGES[-1])

    poster = models.ImageField()
    source_link = models.FileField()


class Translation(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    rate = models.PositiveIntegerField()

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, on_delete=models.SET_NULL, blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)

    translation_link = models.FileField()

    def change_translation_link(self, version):
        pass


class Version(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)

    translation = models.ForeignKey(Translation, on_delete=models.CASCADE)

    version_link = models.FileField()


class RateList(models.Model):
    rate = models.PositiveIntegerField()

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    translation = models.ForeignKey(Translation, on_delete=models.CASCADE)

    def add_rate(self):
        pass

    def change_rate(self):
        pass

    def delete_rate(self):
        pass


class Comment(models.Model):
    description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('Comment', on_delete=models.CASCADE)


class CommentTranslation(models.Model):
    comment = models.OneToOneField(Comment, on_delete=models.CASCADE)
    translation = models.ForeignKey(Translation, on_delete=models.CASCADE)


class CommentOrigin(models.Model):
    comment = models.OneToOneField(Comment, on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
