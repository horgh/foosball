from django.conf.urls.defaults import *
from mysite.foos.models import *

info_dict = {
	'queryset': Team.objects.all(),
}

urlpatterns = patterns('mysite.foos.views',
	(r'^$', 'index'),
	(r'^leaderboard/$', 'leaderboard'),
	(r'^teams/$', 'team_list'),
	(r'^teams/(?P<team_id>\d+)/$', 'team_details'),
	(r'^games/$', 'games'),
)
