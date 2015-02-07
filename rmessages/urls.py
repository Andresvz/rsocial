from django.conf.urls import patterns, url
from .views import MessagesView

urlpatterns = patterns('',

	url(r'^(?P<username>[\w\-]+)/messages/$', MessagesView.as_view(), name='show_messages'),
)