from django.urls import path

from . import views

app_name = 'basic_dashboard'
urlpatterns = [
	path('', views.index),
	path('home', views.index, name='home'),
	path('crypto/<str:crypto>', views.get_crypto, name='get_crypto'),
	path('movie/<str:movie>', views.get_movie, name='get_movie'),
	path('movies/latest_movie', views.get_latest_movie, name='latest_movie'),
	path('movies/popular_movies', views.get_popular_movies, name='popular_movies'),
	path('movies/top_rated_movies', views.get_top_rated_movies, name='top_rated_movies'),
	path('tvshow/<str:tvshow>', views.get_tv_show, name='get_tv_show'),
]
