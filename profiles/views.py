from django.shortcuts import render
from django.views.generic import DetailView
from profiles.models import UserProfile
from buddies.models import Subscription
from datetime import date
from django.contrib.auth.models import User
from django.db.models import Q
from profiles.mixins import UserIdProfileMixin

class ProfileView(UserIdProfileMixin, DetailView):
	model = UserProfile
	template_name = 'profile.html'
	slug_url_kwarg = 'username'
	slug_field = 'user__username'

	# overwritin\ the method of the class DetailView
	def get_context_data(self, **kwargs):
		context = super(ProfileView, self).get_context_data(**kwargs)
		userpro = context.get('userprofile')
		# obteniendo los userprofile_id de los usuarios que tienen amistad con el perfil
		# Get the userprofile_id of users who have friendship with the profile
		list_buddies = self.get_subscription_list(userpro.id)
		# obteniendo los datos de los datos de perfil de los usuarios que pertenecen a los userprofile_id
		# Obtaining data profile data users belonging to the userprofile_id
		buddies = UserProfile.objects.filter(id__in = list_buddies)
		# obteniendo la edad del usuario del perfil visto
		age = self.get_age(userpro.date_birth)
		# obteniendo el id de subcription donde el usuario logueado este relacionado con el usuario del perfil visto
		subscription_id = self.get_subscription_id(userpro.id)
		# 
		is_buddy = self.validate_friendship(userpro.id)
		# actualizando el diccionario context.
		# Updating the context dictionary.
		context.update({'age': age,'buddies': buddies,'is_buddy': is_buddy, 'subscription_id': subscription_id})


		return context

	def get_age(self,date_birth):
		''' calculating age according to date of birth '''

		today = date.today()
		try:
			birthday = date_birth.replace(year = today.year)
		except ValueError:
			birthday = date_birth.replace(year = today.year, month = date_birth.month + 1, day = 1)

		if birthday > today:
			return today.year - date_birth.year - 1
		else:
			return today.year - date_birth.year


	def validate_friendship(self, userproid):
		''' check the user profile is friend or not '''

		userlog_id = self.get_user_id_profile() 

		buddy = self.get_subscription(userproid,userlog_id, True)
		buddy_request = self.get_subscription_request(userproid,userlog_id)
		print (buddy_request)

		# el perfil debe ser diferente al del usuario logueado
		# profile should be different from the logged user
		if userproid != userlog_id:
			if buddy:
				return 'A'
			elif buddy_request:
				if buddy_request == 'you_to_me':
					return 'B'
				else:
					return 'C'
			else:
				return 'D'
		else:
			return None 

	
	def get_subscription_list(self, userproid):
		list_buddies = []

		listbud = Subscription.objects.filter(Q(user = userproid) & Q(status = True)).values('sub_users')
		for i in listbud:
			list_buddies.append(i['sub_users'])

		listbud2 = Subscription.objects.filter(Q(sub_users = userproid) & Q(status = True)).values('user')
		for i in listbud2:
			list_buddies.append(i['user'])

		return list_buddies


	def get_subscription(self, userproid, userlog_id, status):

		value = Subscription.objects.filter(
					Q( Q(user = userproid) & Q(sub_users = userlog_id) & Q(status = status) ) | 
		 			Q( Q(user = userlog_id) & Q(sub_users = userproid) & Q(status = status) ) )
		
		return value

	def get_subscription_request(self, userproid, userlog_id):

		value = Subscription.objects.filter(
					Q( Q(user = userproid) & Q(sub_users = userlog_id) & Q(status = False) ) )

		if value:
			return 'you_to_me'
		else:
			value = Subscription.objects.filter(
					Q( Q(user = userlog_id) & Q(sub_users = userproid) & Q(status = False) ) )
			if value:
				return 'me_to_you'
			else:
				return value


	def get_subscription_id(self,userproid):

		userlog_id = self.get_user_id_profile() 

		subscription_id = Subscription.objects.filter(Q(user = userproid)  & 
							Q(sub_users = userlog_id) & Q(status = True)).values('id')

		if not subscription_id:
			subscription_id = Subscription.objects.filter(Q(user = userlog_id)  & 
							Q(sub_users= userproid) & Q(status = True)).values('id')
		
		for i in subscription_id:
			subscription_id = i['id']

		return subscription_id












	