from django.contrib import admin

from main.models import ShortURL


@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'url', 'times_accessed', 'accessed_at', 'author')
