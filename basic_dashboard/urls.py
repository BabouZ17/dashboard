from django.urls import path

from . import views

app_name = 'basic_dashboard'
urlpatterns = [
	path('', views.index),
	path('home', views.index, name='home'),
	path('weather', views.get_weather, name='get_weather'),
	path('crypto/<str:crypto>', views.get_crypto, name='get_crypto'),
	path('movie/search', views.get_movie, name='get_movie'),
	path('movies/latest_movie', views.get_latest_movie, name='latest_movie'),
	path('movies/popular_movies', views.get_popular_movies, name='popular_movies'),
	path('movies/top_rated_movies', views.get_top_rated_movies, name='top_rated_movies'),
	path('movies/upcoming_movies', views.get_upcoming_movies, name='upcoming_movies'),
	path('movies/now_playing_movies', views.get_now_playing_movies, name='now_playing_movies'),
	path('movie/<str:searched>/reviews', views.get_movie_reviews, name='get_movie_reviews'),
	path('tvshow/search', views.get_tvshow, name='get_tvshow'),
	path('tvshow/latest_tvshow', views.get_latest_tvshow, name='latest_tvshow'),
	path('tvshow/popular_tvshows', views.get_popular_tvshows, name='popular_tvshows'),
	path('tvshow/top_rated_tvshows', views.get_top_rated_tvshow, name='top_rated_tvshows'),
	path('tvshow/upcoming_tvshows', views.get_upcoming_tvshows, name='upcoming_tvshows'),
	path('tvshow/playing_today_tvshows', views.get_playing_today_tvshows, name='playing_today_tvshows'),
	path('tvshow/<str:searched>/reviews', views.get_tvshow_reviews, name='get_tvshow_reviews'),

]
