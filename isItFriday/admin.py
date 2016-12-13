from django.contrib import admin
from .models import GifDate, OnlineGif


class GifDateAdmin(admin.ModelAdmin):
    filter_horizontal = ('gif_urls',)


admin.site.register(GifDate, GifDateAdmin)
admin.site.register(OnlineGif)
