from django.shortcuts import render
from django.views.generic import DetailView
from profiles.models import UserProfile
from datetime import date

# Create your views here.
class ProfileView(DetailView):
	model = UserProfile
	template_name = 'profile.html'
	slug_url_kwarg = 'username'
	slug_field = 'user__username'


	def get_context_data(self, **kwargs):
		context = super(ProfileView, self).get_context_data(**kwargs)
		userpro = context.get('userprofile')
		context.update({'age': self.get_age(userpro.date_birth)})

		return context

	def get_age(self,date_birth):

		today = date.today()
		try:
			birthday = date_birth.replace(year = today.year)
		except ValueError:
			birthday = date_birth.replace(year = today.year, month = date_birth.month + 1, day = 1)

		if birthday > today:
			return today.year - date_birth.year - 1
		else:
			return today.year - date_birth