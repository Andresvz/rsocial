from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30, blank=True)
	avatar = models.ImageField(upload_to = 'avatars/', blank=True)
	date_birth = models.DateField(auto_now_add = False)
	gender = models.CharField(max_length = 50)
	sexual_preference = models.CharField(max_length = 75, blank = True)
	country = models.CharField(max_length = 75)
	about_me = models.TextField(blank = True)
	relationship_status = models.CharField(max_length = 75)
	user = models.OneToOneField(User)

	def __str__(self):
		return self.user.username