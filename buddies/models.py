from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile



class Subscription(models.Model):
    user = models.ForeignKey(User)
    sub_users = models.ManyToManyField(UserProfile, blank=True, null=True, related_name="subscriptions")

    def __str__(self):
    	return self.user.username