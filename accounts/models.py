from django.db import models
from django.contrib.auth.models import User
from main.models import Member

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.OneToOneField(Member, on_delete=models.CASCADE)
