from django.contrib import admin
from .models import AchievementIcon, OriginIcon, UserIcon, OriginFile, VersionFile


class TgFileAdmin(admin.ModelAdmin):
    fields = ('file', 'tg_hash')
    list_display = ('file', 'tg_hash')
    readonly_fields = ('tg_hash',)


class TgImageAdmin(admin.ModelAdmin):
    fields = ('image', 'tg_hash')
    list_display = ('image', 'tg_hash')
    readonly_fields = ('tg_hash',)


admin.site.register(AchievementIcon, TgImageAdmin)
admin.site.register(OriginIcon, TgImageAdmin)
admin.site.register(UserIcon, TgImageAdmin)

admin.site.register(OriginFile, TgFileAdmin)
admin.site.register(VersionFile, TgFileAdmin)
