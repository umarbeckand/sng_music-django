from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from .models import Artist, Song


def home(request):
    """Главная страница"""
    artists_count = Artist.objects.count()
    songs_count = Song.objects.count()
    popular_artists = Artist.objects.annotate(songs_count=Count('songs')).order_by('-songs_count')[:6]
    recent_songs = Song.objects.select_related('artist').order_by('-created_at')[:10]
    
    context = {
        'artists_count': artists_count,
        'songs_count': songs_count,
        'popular_artists': popular_artists,
        'recent_songs': recent_songs,
    }
    return render(request, 'music/home.html', context)


def artists_list(request):
    """Список всех артистов"""
    country = request.GET.get('country', '')
    search = request.GET.get('search', '')
    
    artists = Artist.objects.annotate(songs_count=Count('songs'))
    
    if country:
        artists = artists.filter(country=country)
    
    if search:
        artists = artists.filter(Q(name__icontains=search) | Q(bio__icontains=search))
    
    # Получаем список стран для фильтра
    countries = Artist.objects.values_list('country', flat=True).distinct().order_by('country')
    
    context = {
        'artists': artists,
        'countries': countries,
        'selected_country': country,
        'search_query': search,
    }
    return render(request, 'music/artists_list.html', context)


def artist_detail(request, artist_id):
    """Детальная страница артиста"""
    artist = get_object_or_404(Artist.objects.prefetch_related('songs'), id=artist_id)
    songs = artist.songs.all()
    
    context = {
        'artist': artist,
        'songs': songs,
    }
    return render(request, 'music/artist_detail.html', context)


def songs_list(request):
    """Список всех песен"""
    search = request.GET.get('search', '')
    year = request.GET.get('year', '')
    
    songs = Song.objects.select_related('artist')
    
    if search:
        songs = songs.filter(Q(title__icontains=search) | Q(artist__name__icontains=search))
    
    if year:
        songs = songs.filter(year=year)
    
    # Получаем список годов для фильтра
    years = Song.objects.values_list('year', flat=True).distinct().exclude(year__isnull=True).order_by('-year')
    
    context = {
        'songs': songs,
        'years': years,
        'selected_year': year,
        'search_query': search,
    }
    return render(request, 'music/songs_list.html', context)


def song_detail(request, song_id):
    """Детальная страница песни"""
    song = get_object_or_404(Song.objects.select_related('artist'), id=song_id)
    
    context = {
        'song': song,
    }
    return render(request, 'music/song_detail.html', context)
