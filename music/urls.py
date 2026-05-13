from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.home, name='home'),
    path('artists/', views.artists_list, name='artists_list'),
    path('artists/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('songs/', views.songs_list, name='songs_list'),
    path('songs/<int:song_id>/', views.song_detail, name='song_detail'),
]
