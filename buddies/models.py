from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile



class Subscription(models.Model):

    user = models.ForeignKey(UserProfile, related_name='from_user')
    sub_users = models.ForeignKey(UserProfile, blank=True, null=True, related_name="to_user")
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return str(self.user.first_name + " " + self.user.last_name)