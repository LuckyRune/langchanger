from django.contrib import admin

from .bot import send_image, send_file
from .models import OriginIcon, UserIcon, OriginFile


class TgFileAdmin(admin.ModelAdmin):
    fields = ('tg_hash', 'file')
    list_display = ('tg_hash', 'file')
    readonly_fields = ('tg_hash',)

    def save_model(self, request, obj, form, change):
        file = request.FILES['file']
        model_name = obj.__class__.__name__

        obj.tg_hash = send_file(document=file, chat=model_name)
        super().save_model(request, obj, form, change)


class TgImageAdmin(admin.ModelAdmin):
    fields = ('tg_hash', 'image')
    list_display = ('tg_hash', 'image')
    readonly_fields = ('tg_hash',)

    def save_model(self, request, obj, form, change):
        image = request.FILES['image']
        model_name = obj.__class__.__name__

        obj.tg_hash = send_image(image=image, chat=model_name)
        super().save_model(request, obj, form, change)


admin.site.register(OriginIcon, TgImageAdmin)
admin.site.register(UserIcon, TgImageAdmin)

admin.site.register(OriginFile, TgFileAdmin)
