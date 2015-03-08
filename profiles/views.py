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



	# overwritin the method of the class DetailView
	def get_context_data(self, **kwargs):
		context = super(ProfileView, self).get_context_data(**kwargs)
		userpro = context.get('userprofile')

		# obteniendo el id del perfil al que pertenece el usuario logueado y guardandolo en una variable de clase
		# Getting the id of the profile to which the user belongs and logged in by storing a class variable
		self.userlog_id = self.get_user_id_profile()
		# obteniendo el id del perfil visto en una variable de clase
		# Getting the id of the profile seen in a class variable
		self.userproid = userpro.id

		# obteniendo los userprofile_id de los usuarios que tienen amistad con el perfil
		# Get the userprofile_id of users who have friendship with the profile
		list_buddies = self.get_subscription_list()

		# obteniendo los datos de los datos de perfil de los usuarios que pertenecen a los userprofile_id
		# Obtaining data profile data users belonging to the userprofile_id
		buddies = UserProfile.objects.filter(id__in = list_buddies)
		
		# obteniendo el 4 usuario que han solititado amistad al usuario logueado
		# I getting 4 users who have logged user friendly request
		request = Subscription.objects.filter(Q(sub_users = self.userlog_id) & Q(status = False))	

		# obteniendo la edad del usuario del perfil actualmente visto
		# Obtaining the user's age profile currently seen
		age = self.get_age(userpro.date_birth)

		# obteniendo el id de subcription donde el usuario logueado este relacionado con el usuario del perfil visto
		# Getting the id of the user logged subcription which is related to the user profile seen
		subscription_id = self.get_subscription(True)

		# validando si es amistad, peticion de amistad, o ninguna relacion
		# Validating if friendship, friendship request, or no relationship
		is_buddy = self.validate_friendship()


		# actualizando el diccionario context.
		# Updating the context dictionary.
		context.update({'age': age,'buddies': buddies,'is_buddy': is_buddy, 
			'subscription_id': subscription_id[0].id, 'request': request})


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


	def validate_friendship(self):
		''' check the user profile is friend or not '''

		buddy = self.get_subscription(True)
		buddy_request = self.get_subscription_request()

		# el perfil debe ser diferente al del usuario logueado
		# profile should be different from the logged user
		if self.userproid != self.userlog_id:
			# si buddy existe significa que hay una relacion de amistad
			# if there buddy means there is a friendship
			if buddy:
				return 'A'
			# si buddy_request existe hay una solicitud de amistad
			# if there exists buddy_request a friend request
			elif buddy_request:
				# si esta condicion se cumple la solicitud va de otro usuario al usuario logueado
				# If this condition is met will request another user to user log
				if buddy_request == 'you_to_me':
					return 'B'
				else:
					return 'C'
			# no tienen ninguna relacion 
			# Does not have any relationship
			else:
				return 'D'
		# el usuario del perfil visto es el mismo usuario logueado por lo que no tiene relacion
		# User profile seen is the same user logged in so you have no relationship
		else:
			return None 

	# obteniendo las relaciones de amistad que tiene el usuario logueado ya sea que el envio la peticion o se la enviaron
	# Achieving friendly relations that the user has logged whether sending the request or the sent
	def get_subscription_list(self):
		list_buddies = []
		
		listbud = Subscription.objects.filter(Q(user = self.userproid) & Q(status = True)).values('sub_users')
		for i in listbud:
			list_buddies.append(i['sub_users'])

		listbud2 = Subscription.objects.filter(Q(sub_users = self.userproid) & Q(status = True)).values('user')
		for i in listbud2:
			list_buddies.append(i['user'])

		return list_buddies

	# Obtiene la relacion de amistad si existe entre el usuario logueado y el usuario visto
	# Gets the friendly relationship between the log if user and the user seen
	def get_subscription(self, status):

		value = Subscription.objects.filter(
					Q( Q(user = self.userproid) & Q(sub_users = self.userlog_id) & Q(status = status) ) | 
		 			Q( Q(user = self.userlog_id) & Q(sub_users = self.userproid) & Q(status = status) ) )
		
		return value

	# obtiene las solicitudes de amistad enviadas por el usuario logueado o que le han enviado al usuario logueado
	# obtiene las solicitudes de amistad enviadas por el usuario logueado o que le han enviado al usuario logueado
	def get_subscription_request(self):

		value = Subscription.objects.filter(
					Q( Q(user = self.userproid) & Q(sub_users = self.userlog_id) & Q(status = False) ) )

		if value:
			return 'you_to_me'
		else:
			value = Subscription.objects.filter(
					Q( Q(user = self.userlog_id) & Q(sub_users = self.userproid) & Q(status = False) ) )
			if value:
				return 'me_to_you'
			else:
				return value












	