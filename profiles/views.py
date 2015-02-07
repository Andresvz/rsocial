from django.shortcuts import render
from django.views.generic import DetailView
from profiles.models import UserProfile
from buddies.models import Subscription
from datetime import date
from django.contrib.auth.models import User
from django.db.models import Q

class ProfileView(DetailView):
	model = UserProfile
	template_name = 'profile.html'
	slug_url_kwarg = 'username'
	slug_field = 'user__username'

	# overwritin\ the method of the class DetailView
	def get_context_data(self, **kwargs):
		context = super(ProfileView, self).get_context_data(**kwargs)
		userpro = context.get('userprofile')
		# obteniendo los user_id de los usuarios que tienen amistad con el perfil
		# Get the user_id of users who have friendship with the profile
		list_buddies = Subscription.objects.filter(sub_users = userpro.id).values('user_id')
		# obteniendo los datos de los datos de perfil de los usuarios que pertenecen a los user_id
		# Obtaining data profile data users belonging to the user_id
		buddies = UserProfile.objects.filter(user_id__in = list_buddies)
		# actualizando el diccionario context.
		# Updating the context dictionary.
		context.update({'age': self.get_age(userpro.date_birth),'buddies': buddies})

		listt = Subscription.objects.filter(Q(user = self.request.user.id) & Q(sub_users = userpro.id)).values('sub_users')

		for i in listt:
			print(listt)

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