from django.shortcuts import render
from django.views.generic import DeleteView
from django.views.generic import View
from .models import Subscription
from django.core.urlresolvers import reverse
from profiles.models import UserProfile
from django.http import HttpResponseRedirect
from profiles.mixins import UserIdProfileMixin
from django.db.models import Q

class DeleteBuddy(UserIdProfileMixin, DeleteView):
	model = Subscription
	pk_url_kwarg = 'pk'
	template_name_suffix = '_confirm_delete'

	def get_success_url(self):
		buddy = self.get_user_profile()
		return reverse('show_profile', kwargs={'username': buddy,
		})

 
class AddBuddy(UserIdProfileMixin, View):

	def get(self, request, profile_id, *args, **kwargs):
		buddy = self.get_user_profile()
		buddy2 = UserProfile.objects.get(id = profile_id)
		bud = Subscription(user = buddy, sub_users = buddy2)
		bud.save(force_insert=True)
		return HttpResponseRedirect(reverse('show_profile', kwargs={'username': buddy2,
		}))

class AcceptBuddy(UserIdProfileMixin, View):

	def get(self, request, profile_id, *args, **kwargs):
		buddy = self.get_user_profile()
		buddy2 = UserProfile.objects.get(id = profile_id)
		bud = Subscription.objects.filter(Q(user = buddy2) & Q(sub_users = buddy) & Q(status = False)).update(status= True)
		return HttpResponseRedirect(reverse('show_profile', kwargs={'username': buddy2,
		}))
