from profiles.models import UserProfile

class UserIdProfileMixin(object):

	def get_user_id_profile(self):
		userlog_id = self.get_user_profile()
		return userlog_id.id

	def get_user_profile(self): 
		return UserProfile.objects.get(user= self.request.user.id)

