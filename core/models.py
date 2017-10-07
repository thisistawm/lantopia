from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game = models.CharField(max_length=75, blank=True)
    song = models.CharField(max_length=75, blank=True)
    movie = models.CharField(max_length=75, blank=True)
    tv = models.CharField(max_length=75, blank=True)
    unpacked = models.BooleanField(default=False)


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(user=user)
        user_profile.save()

post_save.connect(create_profile, sender=User)