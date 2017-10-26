from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from core.models import Profile

@login_required
def index(request):
    all_users = User.objects.all().exclude(username="admin").order_by('username')
    return render(request, 'picks/index.html', {'all_users': all_users})

@login_required
def songs(request):
    all_users = User.objects.all().exclude(username="admin").order_by('username')
    return render(request, 'picks/songs.html', {'all_users': all_users})

@login_required
def games(request):
    all_users = User.objects.all().exclude(username="admin").order_by('username')
    return render(request, 'picks/games.html', {'all_users': all_users})

@login_required
def movies(request):
    all_users = User.objects.all().exclude(username="admin").order_by('username')
    return render(request, 'picks/movies.html', {'all_users': all_users})

@login_required
def tv(request):
    all_users = User.objects.all().exclude(username="admin").order_by('username')
    return render(request, 'picks/tv.html', {'all_users': all_users})
