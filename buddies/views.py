from django.shortcuts import render
from django.views.generic import DeleteView
from django.views.generic import View
from .models import Subscription
from django.core.urlresolvers import reverse
from profiles.models import UserProfile
from django.http import HttpResponseRedirect

class DeleteBuddy(DeleteView):
	model = Subscription
	pk_url_kwarg = 'pk'
	template_name_suffix = '_confirm_delete'

	def get_success_url(self):
		buddy = UserProfile.objects.get(user_id = self.request.user.id)
		return reverse('show_profile', kwargs={'username': buddy,
		})


class AddBuddy(View):

	def get(self, request, profile_id, *args, **kwargs):
		buddy = UserProfile.objects.get(user_id = self.request.user.id)
		buddy2 = UserProfile.objects.get(id = profile_id)
		bud = Subscription(user = buddy, sub_users = buddy2)
		bud.save(force_insert=True)
		return HttpResponseRedirect(reverse('show_profile', kwargs={'username': buddy,
		}))

