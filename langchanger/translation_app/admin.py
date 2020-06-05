from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Genre)
admin.site.register(FormatType)
admin.site.register(Language)


@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'description', 'creation_date',
              'genre', ('origin_language', 'format_type'), 'age_limit',
              'poster', 'source_link')
    list_display = ('title', 'author', 'creation_date', 'origin_language', 'format_type')


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    fields = ('author', 'origin', 'language', 'creation_date')
    list_display = ('author', 'language', 'origin', 'creation_date')
    readonly_fields = ('creation_date', )


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    fields = ('translation', 'creation_date', 'version_link')
    list_display = ('translation', 'creation_date')
    readonly_fields = ('creation_date', )


@admin.register(RateList)
class RateListAdmin(admin.ModelAdmin):
    fields = ('rate', 'user', 'translation')
    list_display = ('user', 'translation', 'rate')


@admin.register(CommentOrigin)
class CommentOriginAdmin(admin.ModelAdmin):
    fields = ('author', 'origin', 'post', 'parent_comment', 'post_date')
    list_display = ('author', 'origin', 'parent_comment')
    readonly_fields = ('post_date', )
