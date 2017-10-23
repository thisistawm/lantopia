from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Team(models.Model):
    team_name = models.CharField(max_length=200)
    member1 = models.CharField(max_length=200)
    member2 = models.CharField(max_length=200)
    crypts_wave = models.IntegerField(default=0)
    crypts_remaining = models.IntegerField(default=0)
    def __str__(self):
        return self.team_name

