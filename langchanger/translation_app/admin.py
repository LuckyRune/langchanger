from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Genre)
admin.site.register(Language)


@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    fields = ('title', 'publication_date', 'author', 'description',
              'creation_date', 'genre', 'origin_language',
              'age_limit', 'poster', 'source_link')
    list_display = (
        'title', 'author', 'creation_date', 'origin_language')


@admin.register(CommentOrigin)
class CommentOriginAdmin(admin.ModelAdmin):
    fields = ('author', 'origin', 'post', 'parent_comment', 'post_date')
    list_display = ('author', 'post_date', 'origin', 'parent_comment')
    # readonly_fields = ('post_date', )
