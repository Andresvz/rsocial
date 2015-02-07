from django.db import models
from profiles.models import UserProfile

class UserMessages(models.Model):
    transmitter = models.ManyToManyField(UserProfile, related_name="transmitter")
    receiver = models.ManyToManyField(UserProfile, related_name="receiver")
    message = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
    	return str(self.created)