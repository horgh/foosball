from django.template import *
from django.core.urlresolvers import *
from django.http import *
from django.shortcuts import *
from mysite.foos.models import *

def index(request):
	return render_to_response('foos/index.html')

def leaderboard(request):
	teams = Team.objects.all()
	return render_to_response('foos/leaderboard.html', {'teams': teams})

def team_list(request):
	teams = Team.objects.all()
	return render_to_response('foos/team_list.html', {'team_list': teams})

def team_details(request, team_id):
	team = Team.objects.get(pk=team_id)
	return render_to_response('foos/team_details.html', {'team': team})

def games(request):
	games = Game.objects.order_by('pk').reverse()
	return render_to_response('foos/games.html', {'games': games})
