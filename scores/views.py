from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

from core.models import Profile
from .models import Team

def crypts(request):
    all_users = User.objects.all().exclude(username="admin").order_by('username')
    all_teams = Team.objects.all().order_by('-crypts_wave', 'crypts_remaining')
    return render(request, 'scores/crypts.html', {'all_users': all_users, 'all_teams': all_teams})
