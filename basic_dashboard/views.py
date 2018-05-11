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

def get_popular_movies(request):
	"""
	Get popular movies from moviedb
	"""
	response = requests.get(url=settings.THE_MOVIE_DB_API_URL +
	'/movie/popular?api_key=' + settings.THE_MOVIE_DB_API_KEY)
	context = {
		'data': response.json(),
		'title': 'Popular Movies'
	}
	return render(request, 'movies.html', context)

def get_top_rated_movies(request):
	"""
	Get top rated movies from moviedb
	"""
	response = requests.get(url=settings.THE_MOVIE_DB_API_URL +
	'/movie/top_rated?api_key=' + settings.THE_MOVIE_DB_API_KEY)
	context = {
		'data': response.json(),
		'title': 'Top Rated Movies'
	}
	return render(request, 'movies.html', context)

def get_now_playing_movies(request):
	"""
	Get now playing movies from moviedb
	"""
	response = requests.get(url=settings.THE_MOVIE_DB_API_URL +
	'/movie/now_playing?api_key=' + settings.THE_MOVIE_DB_API_KEY)
	context = {
		'data': response.json(),
		'title': 'Now Playing Movies'
	}
	return render(request, 'movies.html', context)

def get_upcoming_movies(request):
	"""
	Get upcoming movies from moviedb
	"""
	response = requests.get(url=settings.THE_MOVIE_DB_API_URL +
	'/movie/upcoming?api_key=' + settings.THE_MOVIE_DB_API_KEY)
	context = {
		'data': response.json(),
		'title': 'Upcoming Movies'
	}
	return render(request, 'movies.html', context)

def get_movie_reviews(request, id):
	"""
	Get reviews from moviedb according to the id of the movie
	"""
	if request.method == 'POST':
		id = request.POST.get('searched', '')
		response = requests.get(url=settings.THE_MOVIE_DB_API_URL +
		'/movie/' + str(id) + '/reviews?api_key=' + settings.THE_MOVIE_DB_API_KEY +
		'&page=1')
		context = {
			'data': response.json(),
			'title': 'Movie {} Reviews'.format(id),
		}
		return redirect(reverse('basic_dashboard:get_movie_reviews', args=(id,)))
	elif request.method == 'GET':
		assert type(id) is int
		response = requests.get(url=settings.THE_MOVIE_DB_API_URL +
		'/movie/' + str(id) + '/reviews?api_key=' + settings.THE_MOVIE_DB_API_KEY +
		'&page=1')
		context = {
			'data': response.json(),
			'title': 'Movie {} Reviews'.format(id),
		}
		return render(request, 'reviews.html', context)
	else:
		messages.add_message(request, messages.INFO, 'Issue with your request')
		return render(request, 'home.html')

def get_movie(request):
	"""
	Get a searched movie
	"""
	if request.method == 'POST':
		searched = request.POST.get('searched', '')
		response = requests.get(url=settings.THE_MOVIE_DB_API_URL +
		'/search/movie?api_key=' + settings.THE_MOVIE_DB_API_KEY +
		'&language=en-US' + '&query=' + searched + '&page=1')
		context = {
			'data': response.json(),
			'title': 'Movie Search'
		}
		return render(request, 'movies_result.html', context)
	else:
		messages.add_message(request, messages.INFO, 'Issue with your request')
		return render(request, 'home.html')

# TV Shows

def get_tvshow(request):
	"""
	Get a searched tv show
	"""
	if request.method == 'POST':
		searched = request.POST.get('searched', '')
		response = requests.get(url=settings.THE_MOVIE_DB_API_URL +
		'/search/tv?api_key=' + settings.THE_MOVIE_DB_API_KEY +
		'&language=en-US' + '&query=' + searched + '&page=1')
		context = {
			'data': response.json(),
			'title': 'TVShow Search'
		}
		return render(request, 'tvshows.html', context)
	else:
		messages.add_message(request, messages.INFO, 'Issue with your request')
		return render(request, 'home.html')

def get_latest_tvshow(request):
	"""
	Get latest tvshow from moviedb
	"""
	response = requests.get(url=settings.THE_MOVIE_DB_API_URL +
	'/tv/latest?api_key=' + settings.THE_MOVIE_DB_API_KEY)
	context = {
		'data': response.json(),
		'title': 'Latest TV Show'
	}
	return render(request, 'tvshow.html', context)

def get_popular_tvshows(request):
	"""
	Get popular tvshows from moviedb
	"""
	response = requests.get(url=settings.THE_MOVIE_DB_API_URL +
	'/tv/popular?api_key=' + settings.THE_MOVIE_DB_API_KEY)
	context = {
		'data': response.json(),
		'title': 'Popular TVshows'
	}
	return render(request, 'tvshows.html', context)

def get_top_rated_tvshow(request):
	"""
	Get top rated tvshow from moviedb
	"""
	response = requests.get(url=settings.THE_MOVIE_DB_API_URL +
	'/tv/top_rated?api_key=' + settings.THE_MOVIE_DB_API_KEY)
	context = {
		'data': response.json(),
		'title': 'Top Rated TV Shows'
	}
	return render(request, 'tvshows.html', context)

def get_upcoming_tvshows(request):
	"""
	Get upcoming tvshows from moviedb (following week)
	"""
	response = requests.get(url=settings.THE_MOVIE_DB_API_URL +
	'/tv/on_the_air?api_key=' + settings.THE_MOVIE_DB_API_KEY)
	context = {
		'data': response.json(),
		'title': 'Upcoming TV Shows'
	}
	return render(request, 'tvshows.html', context)

def get_playing_today_tvshows(request):
	"""
	Get playing today tvshows from moviedb
	"""
	response = requests.get(url=settings.THE_MOVIE_DB_API_URL +
	'/tv/airing_today?api_key=' + settings.THE_MOVIE_DB_API_KEY)
	context = {
		'data': response.json(),
		'title': 'Airing Today Shows'
	}
	return render(request, 'tvshows.html', context)

def get_tvshow_reviews(request, id):
	"""
	Get reviews from moviedb according to the id of the tvshow
	"""
	if request.method == 'POST':
		id = request.POST.get('searched', '')
		response = requests.get(url=settings.THE_MOVIE_DB_API_URL +
		'/tv/' + str(id) + '/reviews?api_key=' + settings.THE_MOVIE_DB_API_KEY +
		'&page=1')
		context = {
			'data': response.json(),
			'title': 'TV Show {} Reviews'.format(id),
			'test': 'haha'
		}
		return redirect(reverse('basic_dashboard:get_tvshow_reviews', args=(id,)))
	elif request.method == 'GET':
		assert type(id) is int
		response = requests.get(url=settings.THE_MOVIE_DB_API_URL +
		'/tv/' + str(id) + '/reviews?api_key=' + settings.THE_MOVIE_DB_API_KEY +
		'&page=1')
		context = {
			'data': response.json(),
			'title': 'TV Show {} Reviews'.format(id),
		}
		return render(request, 'reviews.html', context)
	else:
		messages.add_message(request, messages.INFO, 'Issue with your request')
		return render(request, 'home.html')

# Domotic
