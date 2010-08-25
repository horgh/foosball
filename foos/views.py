from django.template import *
from django.core.urlresolvers import *
from django.http import *
from django.shortcuts import *
from mysite.foos.models import *
from mysite.foos.models_views import *
from operator import itemgetter

def index(request):
	return render_to_response('foos/index.html')

def leaderboard(request):
	teams = Team.objects.all()
	d = dict()
	for team in teams:
		d[team.name] = team.get_wins()
	sorted_teams = list(reversed(sorted(d.items(), key=itemgetter(1))))
	return render_to_response('foos/leaderboard.html', {'teams': sorted_teams})

def team_list(request):
	teams = Team.objects.all()
	return render_to_response('foos/team_list.html', {'team_list': teams})

def team_details(request, team_id):
	team = Team.objects.get(pk=team_id)
	return render_to_response('foos/team_details.html', {'team': team})

def games(request):
	games = Game.objects.order_by('pk').reverse()
	return render_to_response('foos/games.html', {'games': games})
