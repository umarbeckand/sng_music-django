from django.contrib import admin
from .models import Artist, Song


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'genre', 'created_at']
    list_filter = ['country', 'genre']
    search_fields = ['name', 'bio']
    prepopulated_fields = {'slug': ('name',)} if hasattr(Artist, 'slug') else {}


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'album', 'year']
    list_filter = ['year', 'artist__country']
    search_fields = ['title', 'artist__name', 'album']
    autocomplete_fields = ['artist']
