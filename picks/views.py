from django.shortcuts import render
from django.contrib.auth.models import User

from core.models import Profile


def index(request):
    all_users = User.objects.all().exclude(username="admin").order_by('username')
    return render(request, 'picks/index.html', {'all_users': all_users})

def songs(request):
    all_users = User.objects.all().exclude(username="admin").order_by('username')
    return render(request, 'picks/songs.html', {'all_users': all_users})

def games(request):
    all_users = User.objects.all().exclude(username="admin").order_by('username')
    return render(request, 'picks/games.html', {'all_users': all_users})

def movies(request):
    all_users = User.objects.all().exclude(username="admin").order_by('username')
    return render(request, 'picks/movies.html', {'all_users': all_users})

def tv(request):
    all_users = User.objects.all().exclude(username="admin").order_by('username')
    return render(request, 'picks/tv.html', {'all_users': all_users})
