from django.conf.urls import patterns, url
from .views import ProfileView

urlpatterns = patterns('',

	url(r'^(?P<username>[\w\-]+)/$', ProfileView.as_view(), name='show_profile'),
)