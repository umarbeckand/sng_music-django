from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя артиста')
    photo = models.URLField(max_length=500, blank=True, verbose_name='Фото')
    bio = models.TextField(blank=True, verbose_name='Биография')
    country = models.CharField(max_length=100, verbose_name='Страна')
    genre = models.CharField(max_length=100, blank=True, verbose_name='Жанр')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Артист'
        verbose_name_plural = 'Артисты'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название песни')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs', verbose_name='Артист')
    album = models.CharField(max_length=300, blank=True, verbose_name='Альбом')
    year = models.IntegerField(null=True, blank=True, verbose_name='Год выпуска')
    lyrics = models.TextField(blank=True, verbose_name='Текст песни')
    youtube_url = models.URLField(max_length=500, blank=True, verbose_name='YouTube ссылка')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
        ordering = ['-year', 'title']
    
    def __str__(self):
        return f"{self.title} - {self.artist.name}"
