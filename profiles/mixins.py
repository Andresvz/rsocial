from profiles.models import UserProfile

class UserIdProfileMixin(object):

	def get_user_id_profile(self):
		userlog_id = UserProfile.objects.filter(user = self.request.user.id).values('id')
		for i in userlog_id:
			userlog_id = i['id']
		return userlog_id

	def get_user_profile(self): 
		return UserProfile.objects.get(user= self.request.user.id)

