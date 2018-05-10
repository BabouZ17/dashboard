from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.core import serializers
from django.db.models.base import ObjectDoesNotExist
from django.urls import reverse
from django.conf import settings
from django.contrib import messages

import requests


# Create your views here.

def index(request):
	"""
	Index or home page of the app
	"""
	weather = {'rochefort': '', 'annemasse': '', 'balikpapan': ''}
	for key in weather.keys():
		weather[key] = requests.get(url=settings.WEATHER_API_URL +
		key + '&APPID=' + settings.WEATHER_API_KEY).json()
	return render(request, 'home.html', {'weather_data': weather})

# Cryptos

def get_crypto(request, crypto):
	"""
	Get the crypto intel and global intel
	"""
	result = ''
	global_response = requests.get(url=settings.COIN_MARKET_API_URL +
		'global/').json()

	if request.method == 'GET':
		for key, item in settings.LISTINGS.items():
			if crypto == item or crypto.upper() == item:
				result = str(key)
		if len(result) == 0:
			messages.add_message(request, messages.INFO, 'Unknown Crypto ...')
			context = {
				'crypto_data': '',
				'global_data': global_response
			}
			return render(request, 'crypto.html', context)

		response = requests.get(url=settings.COIN_MARKET_API_URL + 'ticker/'
			+ result + '/').json()
		context = {
			'crypto_data': response,
			'global_data': global_response,
		}
		return render(request, 'crypto.html', context)
	elif request.method == 'POST':
		searched = request.POST.get('searched', '')
		for key, item in settings.LISTINGS.items():
			if searched == item or searched.upper() == item:
				result = str(key)
		if len(result) == 0:
			messages.add_message(request, messages.INFO, 'Unknown Crypto ...')
			context = {
				'crypto_data': '',
				'global_data': global_response
			}
			return render(request, 'crypto.html', context)

		response = requests.get(url=settings.COIN_MARKET_API_URL + 'ticker/'
			+ result + '/').json()
		context = {
			'crypto_data': response,
			'global_data': global_response,
		}
		return redirect(reverse('basic_dashboard:get_crypto', args=(searched,)))

# Movies

def get_latest_movie(request):
	"""
	Get latest movie from moviedb
	"""
	response = requests.get(url=settings.THE_MOVIE_DB_API_URL +
	'/movie/latest?api_key=' + settings.THE_MOVIE_DB_API_KEY)
	context = {
		'data': response.json(),
		'title': 'Latest Movie'
	}
	return render(request, 'movie.html', context)

def get_top_rated_movies(request):
    """
    Get the top rated movies from moviedb
    """
    response = requests.get(url=settings.THE_MOVIE_DB_API_URL + \
	'/movie/top_rated?api_key=' + settings.THE_MOVIE_DB_API_KEY + '&page=1')
    return render(request, 'movies.html', {'data': response.json(), 'title'
	: 'Top Rated Movies'})

def get_popular_movies(request):
    """
    Get the popular movies from moviedb
    """
    response = requests.get(url=settings.THE_MOVIE_DB_API_URL +
	'/movie/popular?api_key=' + settings.THE_MOVIE_DB_API_KEY + '&page=1')
    return render(request, 'movies.html', {'data': response.json(), 'title':
	'Popular Movies'})

def get_now_playing_movies(request):
	"""
	Get the now playing movies from moviedb
	"""
	response = ''
	return render(request, 'movies.html', {'data': response.json(), 'title':
	'Now Playing Movies'})

def get_upcoming_movies(request):
	"""
	Get the upcoming movies from moviedb
	"""
	response = ''
	return render(request, 'movies.html', {'data': response.json(), 'title':
	'Upcoming Movies'})

def get_movie_reviews(request):
	"""
	Get the movie's reviews from moviedb
	"""
	response = ''
	return render(request, 'movies.html', {'data': response.json(), 'title':
	'Movie\'s reviews'})

def get_movie(request, movie):
	"""
	Get a searched movie
	"""
	return render(request, 'home.html')
# TV Shows

def get_tv_show(request, tvshow):
	"""
	Get a searched tv show
	"""
	return render(request, 'home.html')
# Agenda

# Domotic
