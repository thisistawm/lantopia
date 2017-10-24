from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=200, unique=True)
    crypts_wave = models.IntegerField(default=0)
    crypts_remaining = models.IntegerField(default=0)
    players = models.ManyToManyField(User, through='TeamMember')
    def get_players(self):
        return " / ".join([str(p) for p in self.players.all()])
    def __str__(self):
        return self.name
    
class TeamMember(models.Model):
    user = models.ForeignKey(User)
    team = models.ForeignKey(Team) 
