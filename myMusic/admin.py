from django.contrib import admin
from myMusic.models import Playlist, Song


class PlaylistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'playlist', 'url')


admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Song, SongAdmin)