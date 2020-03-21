from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Genre)
admin.site.register(FormatType)
admin.site.register(Language)


@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    fields = ('isbn', 'title', 'author', 'description', 'creation_date',
              'genre', ('origin_language', 'format_type'), 'age_limit',
              'poster', 'source_link')


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    fields = ('author', 'origin', 'language')


@admin.register(RateList)
class RateListAdmin(admin.ModelAdmin):
    fields = ('rate', 'user', 'translation')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('post', 'author', 'parent_comment')


@admin.register(CommentOrigin)
class CommentOriginAdmin(admin.ModelAdmin):
    fields = ('comment', 'origin')
