from django.contrib import admin
from .models import Distrik, Kampung

class tb_distrik(admin.ModelAdmin):
    list_display = ('id_distrik','distrik')
    list_display_links = ('id_distrik','distrik')
    search_fields = ('distrik',)
    list_per_page = 10

class tb_kampung(admin.ModelAdmin):
    list_display = ('id_kampung','distrik','kampung')
    list_display_links = ('id_kampung','distrik','kampung')
    search_fields = ('kampung',)
    list_per_page = 10
    list_filter = ('distrik',)


admin.site.register(Distrik, tb_distrik)
admin.site.register(Kampung, tb_kampung)

