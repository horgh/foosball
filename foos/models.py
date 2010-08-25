from django.db import models
from mysite.foos.models_views import *

class Player(models.Model):
	name = models.CharField(max_length=200)

class Team(models.Model):
	player1 = models.ForeignKey(Player, related_name='player1')
	player2 = models.ForeignKey(Player, related_name='player2')
	name = models.CharField(max_length=200)

	def get_wins(self):
		wins = Wins.objects.filter(pk=self.id)
		if len(wins) == 0:
			return 0L
		else:
			return wins[0].wins

class Game(models.Model):
	team1 = models.ForeignKey(Team, related_name='team1')
	team2 = models.ForeignKey(Team, related_name='team2')

class Score(models.Model):
	game = models.ForeignKey(Game)
	team = models.ForeignKey(Team)
	score = models.IntegerField()
