from django.contrib import admin
from .models import *


class ArtwortkAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.generate_qrcode()
        obj.save()


admin.site.register(Artwortk,ArtwortkAdmin)
admin.site.register(Author)
admin.site.register(Content)
admin.site.register(Page)
admin.site.register(Place)
admin.site.register(Room)
