from django.conf.urls import patterns, url
from .views import DeleteBuddy, AddBuddy

urlpatterns = patterns('',

	url(r'^(?P<username>[\w\-]+)/delbuddy/(?P<pk>\d+)/$', DeleteBuddy.as_view(), name='delete_buddy'),
	url(r'^(?P<username>[\w\-]+)/addbuddy/(?P<profile_id>\d+)/$', AddBuddy.as_view(), name='add_buddy'),
)